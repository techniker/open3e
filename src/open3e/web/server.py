"""FastAPI application factory for the open3e web UI."""

from __future__ import annotations

import importlib.metadata
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, File, HTTPException, Request, UploadFile, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from open3e.web.auth import hash_password, verify_password, SessionManager, AuthMiddleware
from open3e.web.can_discovery import discover_can_interfaces
from open3e.web.config_store import ConfigStore
from open3e.web.ws_manager import WebSocketManager

_HERE = Path(__file__).parent


def create_app(store: ConfigStore) -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(title="open3e Web UI")

    # Mount static files
    static_dir = _HERE / "static"
    if static_dir.exists():
        app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

    # Jinja2 templates
    templates = Jinja2Templates(directory=str(_HERE / "templates"))

    # Store reference on app state
    app.state.store = store

    session_manager = SessionManager()
    app.state.session_manager = session_manager
    app.add_middleware(AuthMiddleware, store=store, session_manager=session_manager)
    app.state.auth_middleware = None  # set after middleware is added

    ws_manager = WebSocketManager()
    app.state.ws_manager = ws_manager

    @app.websocket("/ws")
    async def websocket_endpoint(ws: WebSocket):
        await ws_manager.connect(ws)
        try:
            while True:
                data = await ws.receive_json()
                msg_type = data.get("type")
                if msg_type == "subscribe":
                    dids = data.get("dids", "*")
                    ws_manager.subscribe(ws, dids)
                elif msg_type == "write":
                    engine = getattr(app.state, "engine", None)
                    if engine:
                        engine.send_command({
                            "action": "write_did",
                            "ecu": data["ecu"],
                            "did": data["did"],
                            "value": data["value"],
                            "sub": data.get("sub"),
                        })
        except WebSocketDisconnect:
            ws_manager.disconnect(ws)
        except Exception:
            ws_manager.disconnect(ws)

    # -----------------------------------------------------------------------
    # Auth routes
    # -----------------------------------------------------------------------

    @app.get("/login", response_class=HTMLResponse)
    async def login_page(request: Request):
        return templates.TemplateResponse(request, "login.html", {"error": None})

    @app.post("/login", response_class=HTMLResponse)
    async def login_submit(request: Request):
        form = await request.form()
        password = form.get("password", "")
        stored_hash = await store.get_setting("auth_password_hash")
        if stored_hash and verify_password(password, stored_hash):
            token = session_manager.create_session()
            response = RedirectResponse("/", status_code=302)
            response.set_cookie("open3e_session", token, httponly=True, samesite="lax")
            return response
        return templates.TemplateResponse(request, "login.html", {"error": "Invalid password"})

    @app.post("/api/auth/logout")
    async def logout(request: Request):
        token = request.cookies.get("open3e_session")
        if token:
            session_manager.destroy_session(token)
        from starlette.responses import JSONResponse
        response = JSONResponse({"status": "ok"})
        response.delete_cookie("open3e_session")
        return response

    # -----------------------------------------------------------------------
    # Page routes
    # -----------------------------------------------------------------------

    @app.get("/", response_class=HTMLResponse)
    async def dashboard(request: Request):
        ecus = await store.get_ecus()
        pinned = await store.get_datapoints(poll_priority=3)
        return templates.TemplateResponse(
            request,
            "dashboard.html",
            {"ecus": [dict(e) for e in ecus], "pinned": [dict(dp) for dp in pinned], "active_page": "dashboard"},
        )

    @app.get("/datapoints", response_class=HTMLResponse)
    async def datapoints_page(request: Request):
        ecus = await store.get_ecus()
        datapoints = await store.get_datapoints()
        return templates.TemplateResponse(
            request, "datapoints.html",
            {"ecus": ecus, "datapoints": datapoints, "active_page": "datapoints"},
        )

    @app.get("/settings", response_class=HTMLResponse)
    async def settings_page(request: Request):
        settings = await store.get_all_settings()
        can_interfaces = discover_can_interfaces()
        ha_entities = await store.get_ha_entities()
        backups = await store.list_backups()

        advanced_can_raw = settings.get("advanced_can", "{}")
        try:
            advanced_can = json.loads(advanced_can_raw) if advanced_can_raw else {}
        except (json.JSONDecodeError, TypeError):
            advanced_can = {}

        return templates.TemplateResponse(
            request,
            "settings.html",
            {
                "settings": settings,
                "can_interfaces": can_interfaces,
                "ha_entities": [dict(e) for e in ha_entities],
                "backups": backups,
                "advanced_can": advanced_can,
                "active_page": "settings",
            },
        )

    @app.get("/write", response_class=HTMLResponse)
    async def write_page(request: Request):
        # Load writable DIDs list for filtering
        writable_dids = set()
        writable_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "..", "Open3Edatapoints_writables.json"
        )
        if os.path.isfile(writable_path):
            try:
                with open(writable_path) as wf:
                    writable_dids = set(int(k) for k in json.load(wf).keys())
            except Exception:
                pass
        all_dps = await store.get_datapoints()
        writables = [dp for dp in all_dps if dp["did"] in writable_dids]
        return templates.TemplateResponse(
            request, "write.html",
            {"writables": writables, "active_page": "write"},
        )

    @app.get("/system", response_class=HTMLResponse)
    async def system_page(request: Request):
        import sys as _sys
        try:
            from importlib.metadata import version
            o3e_ver = version("open3e")
        except Exception:
            o3e_ver = "unknown"

        can_iface = await store.get_setting("can_interface", "")
        can_status_data = {"available": False, "interface": can_iface}
        if can_iface:
            from open3e.web.can_discovery import get_can_status
            can_status_data = get_can_status(can_iface)

        engine = getattr(app.state, "engine", None)
        engine_status = engine.get_status() if engine else {
            "state": "idle", "cycle": 0, "ecus_connected": 0, "datapoints_configured": 0
        }

        ecus = await store.get_ecus()

        return templates.TemplateResponse(
            request, "system.html",
            {
                "status": {"open3e_version": o3e_ver, "python_version": _sys.version},
                "can_status": can_status_data,
                "engine_status": engine_status,
                "ecus": ecus,
                "active_page": "system",
            },
        )

    @app.post("/api/write")
    async def write_value(request: Request):
        body = await request.json()
        engine = getattr(app.state, "engine", None)
        if not engine:
            raise HTTPException(status_code=503, detail="CAN engine not running")
        engine.send_command({
            "action": "write_did",
            "ecu": body["ecu"],
            "did": body["did"],
            "value": body["value"],
            "sub": body.get("sub"),
        })
        return {"status": "queued"}

    # -----------------------------------------------------------------------
    # API: settings
    # -----------------------------------------------------------------------

    @app.get("/api/settings")
    async def api_get_settings():
        return await store.get_all_settings()

    @app.patch("/api/settings")
    async def api_patch_settings(request: Request):
        body = await request.json()
        for key, value in body.items():
            # Ensure all values are stored as strings
            if isinstance(value, (dict, list)):
                await store.set_setting(key, json.dumps(value))
            else:
                await store.set_setting(key, str(value))
        # Auto-restart MQTT if MQTT settings changed
        mqtt_keys = {"mqtt_host", "mqtt_port", "mqtt_user", "mqtt_password", "mqtt_tls_enabled", "mqtt_topic_prefix", "mqtt_format_string", "mqtt_client_id"}
        if mqtt_keys.intersection(body.keys()):
            publisher = getattr(app.state, "mqtt_publisher", None)
            if publisher:
                try:
                    await publisher.reconfigure()
                    import logging
                    logging.getLogger(__name__).info("MQTT reconfigured, connected=%s", publisher.connected)
                except Exception as e:
                    import logging
                    logging.getLogger(__name__).error("MQTT reconfigure failed: %s", e)

        # Auto-restart CAN engine if CAN settings changed
        can_keys = {"can_interface", "can_bitrate"}
        if can_keys.intersection(body.keys()):
            start_engine_fn = getattr(app.state, "start_engine", None)
            if start_engine_fn:
                try:
                    can_iface = await store.get_setting("can_interface")
                    can_bitrate_str = await store.get_setting("can_bitrate", "250000")
                    can_bitrate = int(can_bitrate_str) if can_bitrate_str else 250000
                    ecus_list = await store.get_ecus()
                    dp_list = await store.get_datapoints()
                    ecus = [dict(row) for row in ecus_list]
                    datapoints = {row["id"]: dict(row) for row in dp_list}
                    start_engine_fn(can_iface, can_bitrate, ecus, datapoints)
                except Exception:
                    pass

        return {"ok": True}

    # -----------------------------------------------------------------------
    # API: CAN
    # -----------------------------------------------------------------------

    @app.get("/api/can/interfaces")
    async def api_can_interfaces():
        return discover_can_interfaces()

    @app.get("/api/can/status")
    async def api_can_status():
        from open3e.web.can_discovery import get_can_status
        iface = await store.get_setting("can_interface", "")
        if iface:
            return get_can_status(iface)
        return {"available": False, "interface": ""}

    @app.get("/api/engine/values")
    async def api_engine_values():
        """Return all cached DID values from the CAN engine."""
        engine = getattr(app.state, "engine", None)
        if not engine:
            return {}
        # Extract just the values from the cache entries {key: {"value": v, "ts": t}}
        result = {}
        for k, entry in engine._last_values.items():
            if isinstance(entry, dict) and "value" in entry:
                result[k] = entry["value"]
            else:
                result[k] = entry  # backward compat
        return result

    @app.post("/api/engine/reload-schedule")
    async def api_reload_schedule():
        """Reload the engine's polling schedule from the database."""
        engine = getattr(app.state, "engine", None)
        if not engine:
            raise HTTPException(status_code=503, detail="Engine not running")
        dp_rows = await store.get_datapoints()
        datapoints = {row["id"]: dict(row) for row in dp_rows}
        engine.send_command({"action": "update_schedule", "datapoints": datapoints})
        enabled_count = sum(1 for dp in datapoints.values() if dp.get("poll_enabled") and dp.get("poll_priority", 0) > 0)
        return {"ok": True, "total": len(datapoints), "polling": enabled_count}

    @app.get("/api/live-status")
    async def api_live_status():
        """Return current status of CAN, MQTT, and engine for sidebar indicators."""
        from open3e.web.can_discovery import get_can_status
        engine = getattr(app.state, "engine", None)
        publisher = getattr(app.state, "mqtt_publisher", None)
        iface = await store.get_setting("can_interface", "")
        can = get_can_status(iface) if iface else {"available": False}
        return {
            "can": can,
            "mqtt_connected": publisher.connected if publisher else False,
            "engine_state": engine.state.value if engine else "idle",
        }

    # -----------------------------------------------------------------------
    # API: ECUs
    # -----------------------------------------------------------------------

    @app.get("/api/ecus")
    async def api_ecus():
        ecus = await store.get_ecus()
        return [dict(e) for e in ecus]

    # -----------------------------------------------------------------------
    # API: Datapoints
    # -----------------------------------------------------------------------

    @app.get("/api/datapoints")
    async def api_datapoints(ecu: Optional[int] = None, priority: Optional[int] = None):
        dps = await store.get_datapoints(ecu_address=ecu, poll_priority=priority)
        return [dict(dp) for dp in dps]

    @app.patch("/api/datapoints/{dp_id}")
    async def api_patch_datapoint(dp_id: int, request: Request):
        body = await request.json()
        try:
            await store.update_datapoint(dp_id, **body)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc))

        # If poll settings changed, reload the engine's schedule
        if "poll_priority" in body or "poll_enabled" in body:
            engine = getattr(app.state, "engine", None)
            if engine and engine.state.value == "polling":
                dp_rows = await store.get_datapoints()
                engine.send_command({
                    "action": "update_schedule",
                    "datapoints": {row["id"]: dict(row) for row in dp_rows},
                })

        return {"ok": True}

    # -----------------------------------------------------------------------
    # API: HA entities
    # -----------------------------------------------------------------------

    @app.get("/api/ha/entities")
    async def api_ha_entities(enabled: Optional[int] = None):
        entities = await store.get_ha_entities(enabled=enabled)
        return [dict(e) for e in entities]

    @app.patch("/api/ha/entities/{ha_id}")
    async def api_patch_ha_entity(ha_id: int, request: Request):
        body = await request.json()
        try:
            await store.update_ha_entity(ha_id, **body)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc))
        except Exception as exc:
            import logging
            logging.getLogger(__name__).error("HA entity update failed: %s", exc, exc_info=True)
            raise HTTPException(status_code=500, detail=str(exc))
        # Optionally re-publish HA discovery (best-effort, don't fail the request)
        if "enabled" in body:
            try:
                publisher = getattr(app.state, "mqtt_publisher", None)
                if publisher and publisher.connected:
                    entities = await store.get_ha_entities(enabled=1)
                    ecus = await store.get_ecus()
                    tp = await store.get_setting("mqtt_topic_prefix", "vcal")
                    hp = await store.get_setting("ha_discovery_prefix", "homeassistant")
                    publisher.publish_ha_discovery(
                        [dict(e) for e in entities],
                        [dict(e) for e in ecus],
                        tp or "vcal", hp or "homeassistant"
                    )
            except Exception as exc:
                import logging
                logging.getLogger(__name__).warning("HA discovery publish failed: %s", exc)
        return {"ok": True}

    @app.post("/api/ha/apply-defaults")
    async def api_ha_apply_defaults():
        from open3e.web.ha_discovery import infer_ha_entity
        # Only create HA entities for poll-enabled datapoints with priority > 0
        datapoints = await store.get_datapoints()
        active_dps = [dp for dp in datapoints if dp["poll_enabled"] and dp["poll_priority"] > 0]
        created = 0
        for dp in active_dps:
            result = infer_ha_entity(
                dp["name"], dp["codec"] or "", False
            )
            if result:
                ecu_hex = format(dp["ecu_address"], "03x")
                sub = result.get("sub_field") or ""
                uid_parts = ["open3e", ecu_hex, str(dp["did"])]
                if sub:
                    uid_parts.append(sub.lower())
                unique_id = "_".join(uid_parts)
                entity_name = result.get("entity_name") or dp["name"]
                await store.upsert_ha_entity(
                    dp_id=dp["id"],
                    entity_type=result["ha_component"],
                    unique_id=unique_id,
                    name=entity_name,
                    device_class=result.get("device_class"),
                    unit=result.get("unit"),
                    enabled=0,  # default disabled, user enables what they want
                )
                created += 1
        return {"status": "ok", "entities_created": created}
        return {"status": "ok", "entities_created": created}

    # -----------------------------------------------------------------------
    # API: MQTT mappings
    # -----------------------------------------------------------------------

    @app.get("/api/mqtt/mappings")
    async def api_mqtt_mappings(enabled: Optional[int] = None):
        mappings = await store.get_mqtt_mappings(enabled=enabled)
        return [dict(m) for m in mappings]

    @app.post("/api/settings/test-mqtt")
    async def api_test_mqtt(request: Request):
        import paho.mqtt.client as paho_test
        import threading

        body = await request.json()
        host = body.get("mqtt_host", "").strip()
        if not host:
            return {"ok": False, "error": "No MQTT host specified"}
        try:
            port = int(body.get("mqtt_port", 1883))
        except (ValueError, TypeError):
            port = 1883

        result = {"connected": False, "error": None}
        event = threading.Event()

        def on_connect(client, userdata, flags, reason_code, properties=None):
            result["connected"] = True
            event.set()

        def on_connect_fail(client, userdata):
            result["error"] = "Connection refused"
            event.set()

        try:
            client = paho_test.Client(paho_test.CallbackAPIVersion.VERSION2, "open3e_test_" + str(int(__import__("time").time())))
            client.on_connect = on_connect

            user = body.get("mqtt_user", "")
            pw = body.get("mqtt_password", "")
            if user:
                client.username_pw_set(user, pw)

            client.connect(host, port, keepalive=5)
            client.loop_start()

            # Wait up to 5 seconds for the connection callback
            event.wait(timeout=5)
            client.loop_stop()
            client.disconnect()

            if result["connected"]:
                return {"ok": True, "message": "Connected to {}:{}".format(host, port)}
            else:
                return {"ok": False, "error": result["error"] or "Connection timed out after 5 seconds"}
        except Exception as exc:
            return {"ok": False, "error": str(exc)}

    # -----------------------------------------------------------------------
    # API: Backups
    # -----------------------------------------------------------------------

    @app.post("/api/backup")
    async def api_create_backup():
        filename = await store.create_backup()
        return {"filename": filename}

    @app.get("/api/backups")
    async def api_list_backups():
        return await store.list_backups()

    @app.get("/api/backup/{filename}")
    async def api_download_backup(filename: str):
        try:
            path = await store.get_backup_path(filename)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc))
        if not path.exists():
            raise HTTPException(status_code=404, detail="Backup not found")
        return FileResponse(str(path), filename=filename)

    @app.delete("/api/backup/{filename}")
    async def api_delete_backup(filename: str):
        try:
            await store.delete_backup(filename)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc))
        return {"ok": True}

    @app.post("/api/backup/restore")
    async def api_restore_backup(file: UploadFile = File(...)):
        if not (file.filename or "").endswith(".db"):
            raise HTTPException(status_code=400, detail="Only .db files are supported")

        # Write upload to a temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".db") as tmp:
            tmp_path = tmp.name
            content = await file.read()
            tmp.write(content)

        try:
            db_path = store._db_path
            await store.close()
            shutil.copy2(tmp_path, db_path)
            await store.initialize()
        finally:
            os.unlink(tmp_path)

        return {"ok": True, "message": "Restore complete"}

    # -----------------------------------------------------------------------
    # API: Auth settings
    # -----------------------------------------------------------------------

    @app.patch("/api/auth/settings")
    async def api_patch_auth_settings(request: Request):
        body = await request.json()
        if "auth_enabled" in body:
            await store.set_setting("auth_enabled", body["auth_enabled"])
        if "auth_password" in body:
            hashed = hash_password(body["auth_password"])
            await store.set_setting("auth_password_hash", hashed)
        elif "password" in body and body["password"]:
            hashed = hash_password(body["password"])
            await store.set_setting("auth_password_hash", hashed)
        # Invalidate cached auth state
        mw = getattr(app.state, "auth_middleware", None)
        if mw:
            mw.invalidate_cache()
        return {"ok": True}

    # -----------------------------------------------------------------------
    # API: Status
    # -----------------------------------------------------------------------

    @app.get("/api/status")
    async def api_status():
        try:
            open3e_version = importlib.metadata.version("open3e")
        except importlib.metadata.PackageNotFoundError:
            open3e_version = "unknown"
        return {
            "open3e_version": open3e_version,
            "python_version": sys.version,
        }

    # -----------------------------------------------------------------------
    # Page: System Depiction
    # -----------------------------------------------------------------------

    @app.get("/depict", response_class=HTMLResponse)
    async def depict_page(request: Request):
        can_interface = await store.get_setting("can_interface")
        engine = getattr(app.state, "engine", None)
        depict_state = engine.get_depict_state() if engine else {"running": False, "log": [], "returncode": None}
        return templates.TemplateResponse(
            request, "depict.html",
            {
                "can_interface": can_interface,
                "active_page": "depict",
                "depict_state": depict_state,
            },
        )

    # -----------------------------------------------------------------------
    # API: Depiction
    # -----------------------------------------------------------------------

    @app.post("/api/depict/start")
    async def start_depiction(request: Request):
        body = await request.json()
        engine = getattr(app.state, "engine", None)
        if not engine:
            raise HTTPException(status_code=503, detail="Engine not initialized")
        if engine.depict_running:
            raise HTTPException(status_code=409, detail="Scan already running")
        engine.start_depiction(body["can_interface"])
        return {"status": "started"}

    @app.get("/api/depict/status")
    async def depict_status():
        engine = getattr(app.state, "engine", None)
        if not engine:
            return {"running": False, "log": [], "returncode": None}
        return engine.get_depict_state()

    @app.post("/api/depict/cancel")
    async def cancel_depiction():
        engine = getattr(app.state, "engine", None)
        if not engine:
            raise HTTPException(status_code=503, detail="Engine not initialized")
        cancelled = engine.cancel_depiction()
        return {"cancelled": cancelled}

    @app.post("/api/depict/load")
    async def load_depict_results():
        """Load devices.json and datapoint files generated by system depiction."""
        devices_path = "devices.json"
        if not os.path.isfile(devices_path):
            raise HTTPException(status_code=404, detail="devices.json not found")

        with open(devices_path, "r") as f:
            devices = json.load(f)

        # Load the general datapoints table for fallback when device file has None
        import open3e.Open3Edatapoints
        general_dids = dict(open3e.Open3Edatapoints.dataIdentifiers.get("dids", {}))

        # Load writable DIDs list
        writable_dids = set()
        writable_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "..", "Open3Edatapoints_writables.json"
        )
        if os.path.isfile(writable_path):
            try:
                with open(writable_path) as wf:
                    writable_dids = set(int(k) for k in json.load(wf).keys())
            except Exception:
                pass

        total_dps = 0
        for device_key, config in devices.items():
            addr = int(config["tx"], 16) if isinstance(config["tx"], str) else int(config["tx"])
            dp_list = config.get("dpList", "")
            prop = config.get("prop", "")
            # Use device property as name (e.g., "HPMUMASTER") instead of hex key
            ecu_name = prop if prop else device_key
            await store.upsert_ecu(addr, ecu_name, prop, dp_list)

            dp_file = dp_list
            if dp_file and os.path.isfile(dp_file):
                try:
                    import importlib.util
                    spec = importlib.util.spec_from_file_location(
                        "dp_" + dp_file.replace(".", "_"), dp_file
                    )
                    mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(mod)
                    dids = mod.dataIdentifiers.get("dids", {})

                    for did, codec in dids.items():
                        # If codec is None, use the general datapoints table
                        if codec is None:
                            codec = general_dids.get(int(did))
                        if codec is None:
                            await store.upsert_datapoint(
                                ecu_address=addr, did=int(did),
                                name="DID_" + str(did), codec="RawCodec",
                            )
                        else:
                            codec_type_name = type(codec).__name__
                            dp_name = getattr(codec, "id", "DID_" + str(did))
                            await store.upsert_datapoint(
                                ecu_address=addr, did=int(did),
                                name=dp_name, codec=codec_type_name,
                            )
                        total_dps += 1
                except Exception as e:
                    import logging
                    logging.getLogger(__name__).warning("Error loading %s: %s", dp_file, e)

        # Auto-start CAN engine now that we have ECUs and datapoints
        start_engine_fn = getattr(app.state, "start_engine", None)
        if start_engine_fn:
            try:
                can_iface = await store.get_setting("can_interface")
                can_bitrate_str = await store.get_setting("can_bitrate", "250000")
                can_bitrate = int(can_bitrate_str) if can_bitrate_str else 250000
                ecus_list = await store.get_ecus()
                dp_list = await store.get_datapoints()
                ecus = [dict(row) for row in ecus_list]
                datapoints = {row["id"]: dict(row) for row in dp_list}
                start_engine_fn(can_iface, can_bitrate, ecus, datapoints)
            except Exception as e:
                import logging
                logging.getLogger(__name__).warning("Auto-start engine failed: %s", e)

        return {"status": "ok", "devices_loaded": len(devices), "datapoints_loaded": total_dps}

    return app
