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

from open3e.web.auth import hash_password
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
        writables = await store.get_datapoints()
        writables = [dp for dp in writables if dp.get("is_writable")]
        return templates.TemplateResponse(
            request, "write.html",
            {"writables": writables, "active_page": "write"},
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
            await store.set_setting(key, value)
        return {"ok": True}

    # -----------------------------------------------------------------------
    # API: CAN
    # -----------------------------------------------------------------------

    @app.get("/api/can/interfaces")
    async def api_can_interfaces():
        return discover_can_interfaces()

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
        return {"ok": True}

    @app.post("/api/ha/apply-defaults")
    async def api_ha_apply_defaults():
        return {"ok": True, "message": "HA defaults applied (stub)"}

    # -----------------------------------------------------------------------
    # API: MQTT mappings
    # -----------------------------------------------------------------------

    @app.get("/api/mqtt/mappings")
    async def api_mqtt_mappings(enabled: Optional[int] = None):
        mappings = await store.get_mqtt_mappings(enabled=enabled)
        return [dict(m) for m in mappings]

    @app.post("/api/settings/test-mqtt")
    async def api_test_mqtt():
        import paho.mqtt.client as mqtt

        settings = await store.get_all_settings()
        host = settings.get("mqtt_host", "localhost")
        try:
            port = int(settings.get("mqtt_port", 1883))
        except (ValueError, TypeError):
            port = 1883

        client = mqtt.Client()
        try:
            client.connect(host, port, keepalive=5)
            client.disconnect()
            return {"ok": True, "message": f"Connected to {host}:{port}"}
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
        if "password" in body and body["password"]:
            hashed = hash_password(body["password"])
            await store.set_setting("auth_password_hash", hashed)
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

    return app
