"""Launcher — single entry point for the open3e web UI.

This module provides the main() function that:
1. Creates and initializes a ConfigStore
2. Finds an available port
3. Creates the FastAPI app
4. Creates and wires the CAN engine
5. Prints startup information
6. Runs uvicorn
"""

from __future__ import annotations

import asyncio
import socket
import sys

import uvicorn

from open3e.web.can_engine import CanEngine
from open3e.web.config_store import ConfigStore
from open3e.web.mqtt_publisher import MqttPublisher
from open3e.web.server import create_app

DEFAULT_DB_PATH = "open3e_web.db"
DEFAULT_PORT = 8080
MAX_PORT_ATTEMPTS = 10


def _get_local_ip() -> str:
    """Get the local IP address by connecting to a remote socket.

    Falls back to 127.0.0.1 if unable to determine.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
        sock.close()
        return ip
    except Exception:
        return "127.0.0.1"


def _port_available(port: int) -> bool:
    """Check if a port is available by attempting to bind a TCP socket."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("0.0.0.0", port))
        sock.close()
        return True
    except OSError:
        return False


def _find_port(preferred: int) -> int:
    """Find an available port starting from preferred, up to MAX_PORT_ATTEMPTS.

    Returns the first available port found, or raises RuntimeError if none available.
    """
    for offset in range(MAX_PORT_ATTEMPTS):
        candidate = preferred + offset
        if _port_available(candidate):
            return candidate
    raise RuntimeError(
        f"Could not find an available port in range {preferred}-{preferred + MAX_PORT_ATTEMPTS - 1}"
    )


def main() -> None:
    """Main entry point for the open3e web UI."""
    # Create and initialize ConfigStore
    store = ConfigStore(DEFAULT_DB_PATH)
    loop = asyncio.new_event_loop()
    loop.run_until_complete(store.initialize())

    # Read web_port setting from DB (default 8080 if not set)
    preferred_port = loop.run_until_complete(store.get_setting("web_port", DEFAULT_PORT))
    try:
        preferred_port = int(preferred_port)
    except (ValueError, TypeError):
        preferred_port = DEFAULT_PORT

    # Find an available port
    port = _find_port(preferred_port)

    # Create the FastAPI app
    app = create_app(store)

    # Create the CAN engine and attach it to app state
    engine = CanEngine(store)
    app.state.engine = engine

    # Read CAN settings for auto-start
    can_interface = loop.run_until_complete(store.get_setting("can_interface"))
    can_bitrate = loop.run_until_complete(store.get_setting("can_bitrate", 500000))
    ecus_rows = loop.run_until_complete(store.get_ecus())
    datapoints_rows = loop.run_until_complete(store.get_datapoints())

    try:
        can_bitrate = int(can_bitrate)
    except (ValueError, TypeError):
        can_bitrate = 500000

    # Convert DB rows to the dicts expected by CanEngine.start()
    ecus = [dict(row) for row in ecus_rows] if ecus_rows else []
    datapoints = {row["id"]: dict(row) for row in datapoints_rows} if datapoints_rows else {}

    # Determine CAN status for startup message
    can_status = f"CAN: {can_interface}" if can_interface and ecus else "CAN: not configured"

    # Create MQTT publisher
    publisher = MqttPublisher(store, on_status=None)  # on_status wired below after _main_loop is set
    configured = loop.run_until_complete(publisher.configure())
    if configured:
        mqtt_host = loop.run_until_complete(store.get_setting("mqtt_host", "localhost"))
        mqtt_port = loop.run_until_complete(store.get_setting("mqtt_port", 1883))
        try:
            mqtt_port = int(mqtt_port)
        except (ValueError, TypeError):
            mqtt_port = 1883
        publisher.start()
    app.state.mqtt_publisher = publisher

    # Print startup info
    local_ip = _get_local_ip()
    local_url = f"http://127.0.0.1:{port}"
    network_url = f"http://{local_ip}:{port}"
    print(f"Starting open3e web UI", file=sys.stdout)
    print(f"Local:   {local_url}", file=sys.stdout)
    print(f"Network: {network_url}", file=sys.stdout)
    print(f"{can_status}", file=sys.stdout)
    if configured:
        print(f"  MQTT:    {mqtt_host}:{mqtt_port}", file=sys.stdout)
    else:
        print(f"  MQTT:    Not configured", file=sys.stdout)

    # Run uvicorn with an explicit event loop so the engine bridge can schedule
    # async coroutines onto it from the background engine thread.
    _main_loop = None

    def on_mqtt_status(msg: dict) -> None:
        """Bridge: deliver MQTT status to the WebSocket manager on the uvicorn loop."""
        ws_mgr = app.state.ws_manager
        coro = ws_mgr.broadcast_state(msg)
        asyncio.run_coroutine_threadsafe(coro, _main_loop)

    publisher._on_status = on_mqtt_status

    def on_engine_data(msg: dict) -> None:
        """Bridge: deliver engine data to the WebSocket manager on the uvicorn loop."""
        if _main_loop is None:
            return  # Server not ready yet
        ws_mgr = getattr(app.state, "ws_manager", None)
        if ws_mgr is None:
            return
        if msg.get("type") == "did_value":
            coro = ws_mgr.broadcast_did_value(msg)
            # Also publish to MQTT
            publisher.publish_did_value(msg["ecu"], msg["did"], msg.get("name", ""), msg.get("value"))
        else:
            coro = ws_mgr.broadcast_state(msg)
        try:
            asyncio.run_coroutine_threadsafe(coro, _main_loop)
        except RuntimeError:
            pass  # Loop closed

    engine._on_data = on_engine_data

    # Auto-start engine if CAN interface and ECUs are configured
    if can_interface and ecus:
        engine.start(
            can_interface=can_interface,
            can_bitrate=can_bitrate,
            datapoints=datapoints,
            ecus=ecus,
        )

    config = uvicorn.Config(app, host="0.0.0.0", port=port, log_level="warning")
    server = uvicorn.Server(config)

    async def _serve():
        nonlocal _main_loop
        _main_loop = asyncio.get_running_loop()
        await server.serve()

    asyncio.run(_serve())


if __name__ == "__main__":
    main()
