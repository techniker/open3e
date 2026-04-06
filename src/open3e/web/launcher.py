"""Launcher — single entry point for the open3e web UI.

This module provides the main() function that:
1. Creates and initializes a ConfigStore
2. Finds an available port
3. Creates the FastAPI app
4. Prints startup information
5. Runs uvicorn
"""

from __future__ import annotations

import asyncio
import socket
import sys

import uvicorn

from open3e.web.config_store import ConfigStore
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
    asyncio.run(store.initialize())

    # Read web_port setting from DB (default 8080 if not set)
    preferred_port = asyncio.run(store.get_setting("web_port", DEFAULT_PORT))
    try:
        preferred_port = int(preferred_port)
    except (ValueError, TypeError):
        preferred_port = DEFAULT_PORT

    # Find an available port
    port = _find_port(preferred_port)

    # Create the FastAPI app
    app = create_app(store)

    # Print startup info
    local_ip = _get_local_ip()
    local_url = f"http://127.0.0.1:{port}"
    network_url = f"http://{local_ip}:{port}"
    print(f"Starting open3e web UI", file=sys.stdout)
    print(f"Local:   {local_url}", file=sys.stdout)
    print(f"Network: {network_url}", file=sys.stdout)

    # Run uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="warning")


if __name__ == "__main__":
    main()
