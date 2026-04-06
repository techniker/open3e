# Web UI Plan 2: CAN Engine & Live Data

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the CAN engine with priority-based polling, WebSocket live data streaming, interactive dashboard with charts, datapoints browser, write values page, system depiction, and system status.

**Architecture:** The CAN engine runs in a dedicated background thread, communicating with the FastAPI server via `asyncio.Queue`. All O3Eclass/codec access is serialized in the engine thread (thread-safety requirement). WebSocket broadcasts DID values to subscribed browser clients. uPlot renders rolling 30-minute time-series charts in the browser.

**Tech Stack:** Python 3.9+, asyncio.Queue, threading, O3Eclass (existing), FastAPI WebSocket, uPlot (CDN), htmx

**Spec reference:** `docs/specs/2026-04-06-web-ui-design.md`
**Depends on:** Plan 1 (config_store, server, can_discovery, templates, launcher)

---

## File Map

```
src/open3e/web/
  can_engine.py            NEW - CAN/UDS engine + priority scheduler (background thread)
  ws_manager.py            NEW - WebSocket connection manager + broadcast
  server.py                MODIFY - add WebSocket endpoint, depict/status routes, write route
  launcher.py              MODIFY - start CAN engine on startup if configured
  templates/
    dashboard.html       REPLACE - live data cards + uPlot charts
    datapoints.html      NEW - searchable DID table with inline controls
    write.html           NEW - writable DIDs with confirmation
    depict.html          NEW - system depiction with live console
    system.html          NEW - software/CAN/engine/MQTT status
  static/
    js/
      app.js           MODIFY - add WebSocket client helper
      dashboard.js     NEW - dashboard cards, chart management
      datapoints.js    NEW - table filtering, bulk actions

tests/web/
  test_can_engine.py       NEW
  test_ws_manager.py       NEW
  test_server.py           MODIFY - add write, depict, status tests
```

---

### Task 1: WebSocket Connection Manager

**Files:**
- Create: `src/open3e/web/ws_manager.py`
- Create: `tests/web/test_ws_manager.py`

- [ ] **Step 1: Write failing tests**

`tests/web/test_ws_manager.py`:
```python
import asyncio
import pytest
from unittest.mock import AsyncMock, MagicMock
from open3e.web.ws_manager import WebSocketManager


@pytest.fixture
def manager():
    return WebSocketManager()


@pytest.fixture
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


def run(coro):
    return asyncio.get_event_loop().run_until_complete(coro)


def make_ws(accepted=True):
    """Create a mock WebSocket."""
    ws = AsyncMock()
    ws.client_state = MagicMock()
    ws.client_state.name = "CONNECTED"
    return ws


class TestConnect:
    def test_add_client(self, manager):
        ws = make_ws()
        run(manager.connect(ws))
        assert len(manager.clients) == 1

    def test_disconnect_removes_client(self, manager):
        ws = make_ws()
        run(manager.connect(ws))
        manager.disconnect(ws)
        assert len(manager.clients) == 0


class TestSubscribe:
    def test_subscribe_specific_dids(self, manager):
        ws = make_ws()
        run(manager.connect(ws))
        manager.subscribe(ws, [268, 269, 274])
        assert manager.subscriptions[ws] == {268, 269, 274}

    def test_subscribe_all(self, manager):
        ws = make_ws()
        run(manager.connect(ws))
        manager.subscribe(ws, "*")
        assert manager.subscriptions[ws] == "*"

    def test_default_subscribe_all(self, manager):
        ws = make_ws()
        run(manager.connect(ws))
        assert manager.subscriptions[ws] == "*"


class TestBroadcast:
    def test_broadcast_to_subscribed(self, manager):
        ws1 = make_ws()
        ws2 = make_ws()
        run(manager.connect(ws1))
        run(manager.connect(ws2))
        manager.subscribe(ws1, [268])
        manager.subscribe(ws2, [269])

        msg = {"type": "did_value", "did": 268, "value": 27.2}
        run(manager.broadcast_did_value(msg))

        # ws1 subscribed to 268 - should receive
        ws1.send_json.assert_called_once()
        # ws2 subscribed to 269 - should not
        ws2.send_json.assert_not_called()

    def test_broadcast_to_wildcard(self, manager):
        ws = make_ws()
        run(manager.connect(ws))
        manager.subscribe(ws, "*")

        msg = {"type": "did_value", "did": 999, "value": "test"}
        run(manager.broadcast_did_value(msg))
        ws.send_json.assert_called_once()

    def test_broadcast_state(self, manager):
        ws = make_ws()
        run(manager.connect(ws))
        run(manager.broadcast_state({"type": "engine_state", "state": "polling"}))
        ws.send_json.assert_called_once()

    def test_broken_client_removed(self, manager):
        ws = make_ws()
        ws.send_json.side_effect = Exception("connection closed")
        run(manager.connect(ws))
        run(manager.broadcast_state({"type": "engine_state", "state": "idle"}))
        assert len(manager.clients) == 0
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/web/test_ws_manager.py -v
```

- [ ] **Step 3: Implement WebSocketManager**

`src/open3e/web/ws_manager.py`:
```python
"""WebSocket connection manager for live data broadcasting."""

from __future__ import annotations

import logging
from typing import Any, Union

from fastapi import WebSocket

logger = logging.getLogger(__name__)


class WebSocketManager:
    """Manages WebSocket clients with per-client DID subscriptions."""

    def __init__(self):
        self.clients: set[WebSocket] = set()
        self.subscriptions: dict[WebSocket, Union[str, set[int]]] = {}

    async def connect(self, ws: WebSocket) -> None:
        await ws.accept()
        self.clients.add(ws)
        self.subscriptions[ws] = "*"  # default: receive all

    def disconnect(self, ws: WebSocket) -> None:
        self.clients.discard(ws)
        self.subscriptions.pop(ws, None)

    def subscribe(self, ws: WebSocket, dids: Union[str, list[int]]) -> None:
        if dids == "*":
            self.subscriptions[ws] = "*"
        else:
            self.subscriptions[ws] = set(dids)

    async def broadcast_did_value(self, msg: dict[str, Any]) -> None:
        """Send a DID value update to clients subscribed to that DID."""
        did = msg.get("did")
        dead = []
        for ws in list(self.clients):
            sub = self.subscriptions.get(ws, set())
            if sub == "*" or (isinstance(sub, set) and did in sub):
                try:
                    await ws.send_json(msg)
                except Exception:
                    dead.append(ws)
        for ws in dead:
            self.disconnect(ws)

    async def broadcast_state(self, msg: dict[str, Any]) -> None:
        """Send a state update to ALL connected clients."""
        dead = []
        for ws in list(self.clients):
            try:
                await ws.send_json(msg)
            except Exception:
                dead.append(ws)
        for ws in dead:
            self.disconnect(ws)
```

- [ ] **Step 4: Run tests**

```bash
pytest tests/web/test_ws_manager.py -v
```

Expected: All pass.

- [ ] **Step 5: Commit**

```bash
git add src/open3e/web/ws_manager.py tests/web/test_ws_manager.py
git commit -m "Add WebSocket connection manager with per-client DID subscriptions"
```

---

### Task 2: CAN Engine with Priority Scheduler

**Files:**
- Create: `src/open3e/web/can_engine.py`
- Create: `tests/web/test_can_engine.py`

- [ ] **Step 1: Write failing tests**

`tests/web/test_can_engine.py`:
```python
import asyncio
import json
import pytest
import threading
import time
from unittest.mock import MagicMock, patch, AsyncMock

from open3e.web.can_engine import CanEngine, EngineState


@pytest.fixture
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


def run(coro):
    return asyncio.get_event_loop().run_until_complete(coro)


def make_mock_store():
    """Create a mock ConfigStore with async methods."""
    store = MagicMock()
    store.get_setting = AsyncMock(return_value=None)
    store.get_ecus = AsyncMock(return_value=[
        {"address": 0x680, "name": "vitocal", "device_prop": "HPMUMASTER", "dp_list": ""}
    ])
    store.get_datapoints = AsyncMock(return_value=[
        {"id": 1, "ecu_address": 0x680, "did": 268, "name": "FlowTemp",
         "codec_type": "O3EComplexType", "data_length": 9,
         "poll_priority": 3, "poll_enabled": True, "is_writable": False},
        {"id": 2, "ecu_address": 0x680, "did": 377, "name": "IdentNumber",
         "codec_type": "O3EUtf8", "data_length": 14,
         "poll_priority": 1, "poll_enabled": True, "is_writable": False},
    ])
    return store


class TestEngineState:
    def test_initial_state_idle(self):
        store = make_mock_store()
        engine = CanEngine(store)
        assert engine.state == EngineState.IDLE

    def test_state_transitions(self):
        store = make_mock_store()
        engine = CanEngine(store)
        assert engine.state == EngineState.IDLE
        engine._set_state(EngineState.CONNECTING)
        assert engine.state == EngineState.CONNECTING


class TestPriorityScheduler:
    def test_build_cycle_high_only(self):
        store = make_mock_store()
        engine = CanEngine(store)
        engine._datapoints = {
            (0x680, 268): {"priority": 3, "did": 268, "ecu": 0x680},
        }
        cycle_list = engine._build_poll_list(cycle=1)
        assert len(cycle_list) == 1  # high only on cycle 1

    def test_build_cycle_with_medium(self):
        store = make_mock_store()
        engine = CanEngine(store)
        engine._datapoints = {
            (0x680, 268): {"priority": 3, "did": 268, "ecu": 0x680},
            (0x680, 318): {"priority": 2, "did": 318, "ecu": 0x680},
        }
        cycle_list = engine._build_poll_list(cycle=3)
        assert len(cycle_list) == 2  # high + medium on cycle 3

    def test_build_cycle_with_all(self):
        store = make_mock_store()
        engine = CanEngine(store)
        engine._datapoints = {
            (0x680, 268): {"priority": 3, "did": 268, "ecu": 0x680},
            (0x680, 318): {"priority": 2, "did": 318, "ecu": 0x680},
            (0x680, 377): {"priority": 1, "did": 377, "ecu": 0x680},
        }
        cycle_list = engine._build_poll_list(cycle=0)
        assert len(cycle_list) == 3  # all on cycle 0

    def test_disabled_excluded(self):
        store = make_mock_store()
        engine = CanEngine(store)
        engine._datapoints = {
            (0x680, 268): {"priority": 0, "did": 268, "ecu": 0x680},
        }
        cycle_list = engine._build_poll_list(cycle=0)
        assert len(cycle_list) == 0


class TestCommandQueue:
    def test_enqueue_command(self):
        store = make_mock_store()
        engine = CanEngine(store)
        engine.send_command({"action": "read_did", "ecu": 0x680, "did": 268})
        assert not engine._cmd_queue.empty()

    def test_dequeue_command(self):
        store = make_mock_store()
        engine = CanEngine(store)
        engine.send_command({"action": "stop"})
        cmd = engine._cmd_queue.get_nowait()
        assert cmd["action"] == "stop"


class TestDataQueue:
    def test_data_callback(self):
        store = make_mock_store()
        received = []
        engine = CanEngine(store, on_data=lambda msg: received.append(msg))
        engine._emit_data({"type": "did_value", "did": 268, "value": 27.2})
        assert len(received) == 1
        assert received[0]["did"] == 268
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/web/test_can_engine.py -v
```

- [ ] **Step 3: Implement CAN Engine**

`src/open3e/web/can_engine.py`:
```python
"""CAN engine - background thread for CAN/UDS communication with priority scheduler.

THREAD SAFETY: All O3Eclass and Open3Ecodecs access is confined to this engine's
thread. The web server communicates exclusively via command/data queues.
"""

from __future__ import annotations

import enum
import logging
import queue
import subprocess
import threading
import time
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

# Priority scheduler constants
CYCLE_LENGTH = 12
MEDIUM_INTERVAL = 4   # medium polled every 4th cycle
LOW_INTERVAL = 12     # low polled every 12th cycle
INTER_DID_DELAY = 0.02  # 20ms between UDS requests


class EngineState(enum.Enum):
    IDLE = "idle"
    CONNECTING = "connecting"
    POLLING = "polling"
    PAUSED = "paused"
    EXECUTING_COMMAND = "executing_command"


class CanEngine:
    """Background CAN/UDS engine with priority-based polling.

    All CAN communication happens in a dedicated thread. The web server
    sends commands via send_command() and receives data via the on_data callback.
    """

    def __init__(self, store, on_data: Optional[Callable] = None):
        self.store = store
        self._on_data = on_data
        self._state = EngineState.IDLE
        self._state_lock = threading.Lock()
        self._cmd_queue: queue.Queue = queue.Queue()
        self._thread: Optional[threading.Thread] = None
        self._running = False
        self._cycle = 0
        self._ecus: dict[int, Any] = {}  # addr -> O3Eclass instance
        self._datapoints: dict[tuple[int, int], dict] = {}  # (ecu, did) -> info
        self._last_values: dict[tuple[int, int], Any] = {}  # (ecu, did) -> last value
        self._depict_process: Optional[subprocess.Popen] = None

    @property
    def state(self) -> EngineState:
        with self._state_lock:
            return self._state

    def _set_state(self, state: EngineState) -> None:
        with self._state_lock:
            self._state = state
        self._emit_data({"type": "engine_state", "state": state.value})

    def _emit_data(self, msg: dict) -> None:
        if self._on_data:
            try:
                self._on_data(msg)
            except Exception as e:
                logger.error(f"Error in data callback: {e}")

    def send_command(self, cmd: dict) -> None:
        """Send a command to the engine (thread-safe)."""
        self._cmd_queue.put(cmd)

    def get_last_value(self, ecu: int, did: int) -> Any:
        """Get the last known value for a datapoint."""
        return self._last_values.get((ecu, did))

    # --- Priority Scheduler ---

    def _build_poll_list(self, cycle: int) -> list[dict]:
        """Build the list of datapoints to poll this cycle."""
        high = []
        medium = []
        low = []
        for key, dp in self._datapoints.items():
            prio = dp["priority"]
            if prio == 3:
                high.append(dp)
            elif prio == 2:
                medium.append(dp)
            elif prio == 1:
                low.append(dp)
            # prio == 0: disabled, skip

        result = list(high)
        if cycle % MEDIUM_INTERVAL == 0:
            result.extend(medium)
        if cycle % LOW_INTERVAL == 0:
            result.extend(low)
        return result

    # --- Thread Entry Point ---

    def start(self, can_interface: str, can_bitrate: int = 250000,
              datapoints: Optional[list[dict]] = None,
              ecus: Optional[list[dict]] = None) -> None:
        """Start the engine in a background thread."""
        if self._thread and self._thread.is_alive():
            logger.warning("Engine already running")
            return

        self._running = True

        # Store datapoint config
        if datapoints:
            self._datapoints = {}
            for dp in datapoints:
                key = (dp["ecu_address"], dp["did"])
                self._datapoints[key] = {
                    "ecu": dp["ecu_address"],
                    "did": dp["did"],
                    "name": dp.get("name", f"DID_{dp['did']}"),
                    "priority": dp.get("poll_priority", 1),
                }

        self._thread = threading.Thread(
            target=self._run,
            args=(can_interface, can_bitrate, ecus or []),
            daemon=True,
            name="can-engine",
        )
        self._thread.start()

    def stop(self) -> None:
        """Stop the engine."""
        self._running = False
        self.send_command({"action": "stop"})
        if self._thread:
            self._thread.join(timeout=5)
            self._thread = None
        self._set_state(EngineState.IDLE)

    def _run(self, can_interface: str, can_bitrate: int, ecus_config: list[dict]) -> None:
        """Engine main loop (runs in background thread)."""
        self._set_state(EngineState.CONNECTING)

        # Try to create O3Eclass instances for each ECU
        try:
            import open3e.Open3Eclass
            for ecu_cfg in ecus_config:
                addr = ecu_cfg["address"]
                dp_list = ecu_cfg.get("dp_list", "")
                dev = dp_list if dp_list else None
                try:
                    ecu = open3e.Open3Eclass.O3Eclass(
                        ecutx=addr, can=can_interface, dev=dev
                    )
                    self._ecus[addr] = ecu
                    logger.info(f"Connected to ECU {hex(addr)}")
                except Exception as e:
                    logger.error(f"Failed to connect to ECU {hex(addr)}: {e}")
                    self._emit_data({
                        "type": "error",
                        "message": f"Failed to connect to ECU {hex(addr)}: {e}",
                    })
        except ImportError as e:
            logger.error(f"Cannot import O3Eclass: {e}")
            self._emit_data({
                "type": "error",
                "message": f"CAN communication unavailable: {e}",
            })
            self._set_state(EngineState.IDLE)
            return

        if not self._ecus:
            self._emit_data({
                "type": "error",
                "message": "No ECUs connected. Check CAN interface and run System Depiction.",
            })
            self._set_state(EngineState.IDLE)
            return

        self._set_state(EngineState.POLLING)
        self._cycle = 0

        while self._running:
            # Check command queue between every operation
            self._process_commands()

            if self.state == EngineState.PAUSED:
                time.sleep(0.1)
                continue

            if self.state != EngineState.POLLING:
                time.sleep(0.1)
                continue

            # Build poll list for this cycle
            poll_list = self._build_poll_list(self._cycle)

            for dp in poll_list:
                if not self._running:
                    break

                # Check for commands between each DID read
                self._process_commands()
                if self.state != EngineState.POLLING:
                    break

                ecu_addr = dp["ecu"]
                did = dp["did"]
                ecu = self._ecus.get(ecu_addr)
                if not ecu:
                    continue

                try:
                    value, idstr, idid = ecu.readByDid(did, raw=False)
                    ts = int(time.time())
                    self._last_values[(ecu_addr, did)] = value

                    self._emit_data({
                        "type": "did_value",
                        "ecu": ecu_addr,
                        "did": did,
                        "name": dp.get("name", idstr),
                        "value": value,
                        "ts": ts,
                    })
                except Exception as e:
                    logger.warning(f"Error reading {hex(ecu_addr)}.{did}: {e}")
                    self._emit_data({
                        "type": "did_value",
                        "ecu": ecu_addr,
                        "did": did,
                        "name": dp.get("name", f"DID_{did}"),
                        "value": f"ERR: {e}",
                        "ts": int(time.time()),
                    })

                time.sleep(INTER_DID_DELAY)

            self._cycle = (self._cycle + 1) % CYCLE_LENGTH

        # Cleanup
        self._cleanup()

    def _process_commands(self) -> None:
        """Process all pending commands from the queue."""
        while not self._cmd_queue.empty():
            try:
                cmd = self._cmd_queue.get_nowait()
            except queue.Empty:
                break

            action = cmd.get("action")

            if action == "stop":
                self._running = False

            elif action == "pause":
                self._set_state(EngineState.PAUSED)

            elif action == "resume":
                self._set_state(EngineState.POLLING)

            elif action == "read_did":
                self._handle_read(cmd)

            elif action == "write_did":
                self._handle_write(cmd)

            elif action == "update_schedule":
                self._handle_update_schedule(cmd)

    def _handle_read(self, cmd: dict) -> None:
        """Handle an on-demand read request."""
        prev_state = self.state
        self._set_state(EngineState.EXECUTING_COMMAND)
        ecu_addr = cmd["ecu"]
        did = cmd["did"]
        ecu = self._ecus.get(ecu_addr)
        if ecu:
            try:
                value, idstr, idid = ecu.readByDid(did, raw=False)
                self._last_values[(ecu_addr, did)] = value
                self._emit_data({
                    "type": "did_value",
                    "ecu": ecu_addr,
                    "did": did,
                    "name": idstr,
                    "value": value,
                    "ts": int(time.time()),
                })
            except Exception as e:
                self._emit_data({
                    "type": "error",
                    "message": f"Read error {hex(ecu_addr)}.{did}: {e}",
                })
        self._set_state(prev_state)

    def _handle_write(self, cmd: dict) -> None:
        """Handle a write request."""
        prev_state = self.state
        self._set_state(EngineState.EXECUTING_COMMAND)
        ecu_addr = cmd["ecu"]
        did = cmd["did"]
        value = cmd["value"]
        sub = cmd.get("sub")
        ecu = self._ecus.get(ecu_addr)
        result = {"type": "write_result", "ecu": ecu_addr, "did": did, "success": False}
        if ecu:
            try:
                succ, code = ecu.writeByDid(did, value, raw=False, sub=sub)
                result["success"] = succ
                result["code"] = str(code)
            except Exception as e:
                result["error"] = str(e)
        else:
            result["error"] = f"ECU {hex(ecu_addr)} not connected"
        self._emit_data(result)
        self._set_state(prev_state)

    def _handle_update_schedule(self, cmd: dict) -> None:
        """Update the polling schedule from the database."""
        datapoints = cmd.get("datapoints", [])
        self._datapoints = {}
        for dp in datapoints:
            key = (dp["ecu_address"], dp["did"])
            self._datapoints[key] = {
                "ecu": dp["ecu_address"],
                "did": dp["did"],
                "name": dp.get("name", f"DID_{dp['did']}"),
                "priority": dp.get("poll_priority", 1),
            }

    def _cleanup(self) -> None:
        """Close all ECU connections."""
        for addr, ecu in self._ecus.items():
            try:
                ecu.close()
                logger.info(f"Closed ECU {hex(addr)}")
            except Exception as e:
                logger.warning(f"Error closing ECU {hex(addr)}: {e}")
        self._ecus.clear()
        self._set_state(EngineState.IDLE)

    # --- System Depiction ---

    def start_depiction(self, can_interface: str, on_line: Optional[Callable] = None) -> None:
        """Start system depiction as a subprocess."""
        if self._depict_process and self._depict_process.poll() is None:
            return  # already running

        # Pause polling if active
        if self.state == EngineState.POLLING:
            self.send_command({"action": "pause"})
            time.sleep(0.2)

        cmd = ["open3e_depictSystem", "-c", can_interface]
        self._depict_process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )

        def _reader():
            for line in self._depict_process.stdout:
                line = line.rstrip()
                if on_line:
                    on_line(line)
                self._emit_data({"type": "depict_progress", "line": line})
            self._depict_process.wait()
            self._emit_data({
                "type": "depict_complete",
                "returncode": self._depict_process.returncode,
            })

        threading.Thread(target=_reader, daemon=True, name="depict-reader").start()

    @property
    def depict_running(self) -> bool:
        return self._depict_process is not None and self._depict_process.poll() is None

    # --- Status ---

    def get_status(self) -> dict:
        """Return current engine status."""
        return {
            "state": self.state.value,
            "cycle": self._cycle,
            "ecus_connected": len(self._ecus),
            "datapoints_configured": len(self._datapoints),
            "depict_running": self.depict_running,
        }
```

- [ ] **Step 4: Run tests**

```bash
pytest tests/web/test_can_engine.py -v
```

Expected: All pass.

- [ ] **Step 5: Commit**

```bash
git add src/open3e/web/can_engine.py tests/web/test_can_engine.py
git commit -m "Add CAN engine with priority scheduler and command queue"
```

---

### Task 3: WebSocket Endpoint + App.js Client

**Files:**
- Modify: `src/open3e/web/server.py`
- Modify: `src/open3e/web/static/js/app.js`

- [ ] **Step 1: Add WebSocket endpoint to server.py**

Add these imports at the top of `server.py`:
```python
from fastapi import WebSocket, WebSocketDisconnect
from open3e.web.ws_manager import WebSocketManager
```

Add to `create_app()`, after the store assignment:
```python
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
```

- [ ] **Step 2: Add WebSocket client helper to app.js**

Append to `src/open3e/web/static/js/app.js`:
```javascript

/**
 * WebSocket client for live data.
 * Usage:
 *   const ws = openWebSocket();
 *   ws.onDidValue = (msg) => { ... };
 *   ws.onEngineState = (msg) => { ... };
 *   ws.subscribe([268, 269]);  // or ws.subscribe("*")
 */
function openWebSocket() {
    const protocol = location.protocol === "https:" ? "wss:" : "ws:";
    const url = protocol + "//" + location.host + "/ws";
    const socket = new WebSocket(url);
    const api = {
        socket: socket,
        _closed: false,
        onDidValue: null,
        onEngineState: null,
        onCanStatus: null,
        onMqttStatus: null,
        onDepictProgress: null,
        onDepictComplete: null,
        onWriteResult: null,
        onError: null,

        subscribe(dids) {
            if (socket.readyState === WebSocket.OPEN) {
                socket.send(JSON.stringify({ type: "subscribe", dids: dids }));
            }
        },
        write(ecu, did, value, sub) {
            const msg = { type: "write", ecu: ecu, did: did, value: value };
            if (sub) msg.sub = sub;
            socket.send(JSON.stringify(msg));
        },
        close() {
            api._closed = true;
            socket.close();
        }
    };

    socket.onmessage = function(event) {
        const msg = JSON.parse(event.data);
        switch (msg.type) {
            case "did_value":
                if (api.onDidValue) api.onDidValue(msg);
                break;
            case "engine_state":
                if (api.onEngineState) api.onEngineState(msg);
                updateStatusIndicators(msg);
                break;
            case "can_status":
                if (api.onCanStatus) api.onCanStatus(msg);
                break;
            case "mqtt_status":
                if (api.onMqttStatus) api.onMqttStatus(msg);
                break;
            case "depict_progress":
                if (api.onDepictProgress) api.onDepictProgress(msg);
                break;
            case "depict_complete":
                if (api.onDepictComplete) api.onDepictComplete(msg);
                break;
            case "write_result":
                if (api.onWriteResult) api.onWriteResult(msg);
                break;
            case "error":
                if (api.onError) api.onError(msg);
                showToast(msg.message || "Engine error", "danger");
                break;
        }
    };

    socket.onclose = function() {
        // Auto-reconnect after 3 seconds
        setTimeout(function() {
            if (!api._closed) openWebSocket();
        }, 3000);
    };

    return api;
}

/**
 * Update sidebar status indicators from engine state messages.
 */
function updateStatusIndicators(msg) {
    const canDot = document.getElementById("status-can");
    const canText = document.getElementById("status-can-text");
    const engineDot = document.getElementById("status-engine");
    const engineText = document.getElementById("status-engine-text");

    if (!engineDot) return;

    const state = msg.state || msg.engine_state;
    if (state === "polling") {
        engineDot.className = "status-dot green";
        engineText.textContent = "Polling";
        if (canDot) { canDot.className = "status-dot green"; canText.textContent = "Connected"; }
    } else if (state === "connecting") {
        engineDot.className = "status-dot amber";
        engineText.textContent = "Connecting";
    } else if (state === "paused") {
        engineDot.className = "status-dot amber";
        engineText.textContent = "Paused";
    } else if (state === "idle") {
        engineDot.className = "status-dot gray";
        engineText.textContent = "Idle";
        if (canDot) { canDot.className = "status-dot gray"; canText.textContent = "--"; }
    } else {
        engineDot.className = "status-dot amber";
        engineText.textContent = state;
    }
}
```

- [ ] **Step 3: Commit**

```bash
git add src/open3e/web/server.py src/open3e/web/static/js/app.js
git commit -m "Add WebSocket endpoint and client-side connection helper with auto-reconnect"
```

---

### Task 4: Wire Engine into Launcher

**Files:**
- Modify: `src/open3e/web/launcher.py`

- [ ] **Step 1: Update launcher to start engine and wire data callback**

Replace the `main()` function in `launcher.py` with the version that:
1. Creates a `CanEngine(store)` instance
2. Stores it on `app.state.engine`
3. Sets up `on_engine_data` callback that bridges engine thread data to WebSocket via `asyncio.run_coroutine_threadsafe()`
4. Auto-starts the engine if CAN interface and ECUs are configured in the DB
5. Runs uvicorn via `uvicorn.Server` + `asyncio.run()` to capture the main event loop for cross-thread scheduling

Key implementation detail for the cross-thread bridge:

```python
    # Global to capture uvicorn's event loop
    _main_loop = None

    def on_engine_data(msg):
        """Bridge engine data to WebSocket clients (called from engine thread)."""
        ws_mgr = getattr(app.state, "ws_manager", None)
        if ws_mgr is None or _main_loop is None:
            return
        if msg.get("type") == "did_value":
            coro = ws_mgr.broadcast_did_value(msg)
        else:
            coro = ws_mgr.broadcast_state(msg)
        asyncio.run_coroutine_threadsafe(coro, _main_loop)

    engine._on_data = on_engine_data

    # Use uvicorn.Server to capture event loop
    config = uvicorn.Config(app, host="0.0.0.0", port=port, log_level="warning")
    server = uvicorn.Server(config)

    async def _serve():
        nonlocal _main_loop
        _main_loop = asyncio.get_running_loop()
        await server.serve()

    asyncio.run(_serve())
```

- [ ] **Step 2: Commit**

```bash
git add src/open3e/web/launcher.py
git commit -m "Wire CAN engine into launcher with auto-start and WebSocket data bridge"
```

---

### Task 5: Dashboard Template with uPlot Charts

**Files:**
- Replace: `src/open3e/web/templates/dashboard.html`
- Create: `src/open3e/web/static/js/dashboard.js`
- Modify: `src/open3e/web/server.py` (update dashboard route to pass pinned datapoints)

- [ ] **Step 1: Create dashboard.js**

Create `src/open3e/web/static/js/dashboard.js` with:
- WebSocket connection on DOMContentLoaded, subscribing to all DIDs
- `handleDidValue(msg)` - updates card value display and feeds chart data
- `handleEngineState(msg)` - updates engine badge
- `formatValue(value)` - extracts display value from complex types (prefers "Actual" sub-field)
- `extractNumeric(value)` - extracts numeric value for charting
- `toggleChart(ecu, did, name)` - creates/destroys uPlot chart in a container div
- uPlot config: dark theme grid colors, 200px height, auto-resize via ResizeObserver
- Chart data: rolling 30-min window (MAX_POINTS=1800), shifts old data out

- [ ] **Step 2: Replace dashboard.html**

Create template that:
- Extends base.html, includes uPlot CSS+JS from CDN (v1.6.30)
- Shows warning if no ECUs, info if no pinned datapoints
- Renders a card grid from `pinned` template var (datapoints with poll_priority=3)
- Each card: name, ECU.DID, value display, timestamp, click to toggle chart
- Chart container div below each card (hidden by default)

- [ ] **Step 3: Update dashboard route in server.py**

```python
    @app.get("/", response_class=HTMLResponse)
    async def dashboard(request: Request):
        ecus = await store.get_ecus()
        pinned = await store.get_datapoints(poll_priority=3)
        return templates.TemplateResponse(
            request, "dashboard.html",
            {"ecus": ecus, "pinned": pinned, "active_page": "dashboard"},
        )
```

- [ ] **Step 4: Commit**

```bash
git add src/open3e/web/templates/dashboard.html src/open3e/web/static/js/dashboard.js src/open3e/web/server.py
git commit -m "Add live dashboard with uPlot charts and WebSocket data streaming"
```

---

### Task 6: Datapoints Browser Page

**Files:**
- Create: `src/open3e/web/templates/datapoints.html`
- Create: `src/open3e/web/static/js/datapoints.js`
- Modify: `src/open3e/web/server.py` (add `/datapoints` page route)

- [ ] **Step 1: Create datapoints.js** with search filtering, priority/polling controls, bulk actions
- [ ] **Step 2: Create datapoints.html** with searchable table, ECU/priority filters, inline controls
- [ ] **Step 3: Add datapoints route to server.py**
- [ ] **Step 4: Commit**

```bash
git add src/open3e/web/templates/datapoints.html src/open3e/web/static/js/datapoints.js src/open3e/web/server.py
git commit -m "Add datapoints browser with search, filter, priority control, and live values"
```

---

### Task 7: Write Values Page

**Files:**
- Create: `src/open3e/web/templates/write.html`
- Modify: `src/open3e/web/server.py` (add `/write` route, `POST /api/write`)

- [ ] **Step 1: Create write.html** with writable DIDs table, value input, confirmation modal, WebSocket write result handling
- [ ] **Step 2: Add routes to server.py** (`GET /write`, `POST /api/write`)
- [ ] **Step 3: Commit**

```bash
git add src/open3e/web/templates/write.html src/open3e/web/server.py
git commit -m "Add write values page with confirmation dialog and CAN engine integration"
```

---

### Task 8: System Depiction Page

**Files:**
- Create: `src/open3e/web/templates/depict.html`
- Modify: `src/open3e/web/server.py` (add `/depict` route, depict API endpoints)

- [ ] **Step 1: Create depict.html** with CAN interface input, start scan button, live console output area (uses textContent, not innerHTML), load results button
- [ ] **Step 2: Add routes** (`GET /depict`, `POST /api/depict/start`, `GET /api/depict/status`, `POST /api/depict/load`)
- [ ] **Step 3: The `/api/depict/load` endpoint** reads `devices.json`, imports datapoint files, populates ECUs and datapoints tables, loads writable list from `Open3Edatapoints_writables.json`
- [ ] **Step 4: Commit**

```bash
git add src/open3e/web/templates/depict.html src/open3e/web/server.py
git commit -m "Add system depiction page with live console output and result loading"
```

---

### Task 9: System Status Page

**Files:**
- Create: `src/open3e/web/templates/system.html`
- Modify: `src/open3e/web/server.py` (add `/system` route)

- [ ] **Step 1: Create system.html** with cards for Software (versions), CAN Bus (interface, state, counters), Engine (state, cycle, ECUs, datapoints), ECU list table
- [ ] **Step 2: Add system route** using `get_can_status()`, `engine.get_status()`, `store.get_ecus()`
- [ ] **Step 3: Commit**

```bash
git add src/open3e/web/templates/system.html src/open3e/web/server.py
git commit -m "Add system status page with software, CAN, engine, and ECU information"
```

---

### Task 10: Run all tests and verify

- [ ] **Step 1: Run the complete test suite**

```bash
pytest tests/web/ -v
```

Expected: All tests pass (existing + new).

- [ ] **Step 2: Verify all pages render without errors**

```bash
python -c "
import asyncio
from open3e.web.config_store import ConfigStore
from open3e.web.server import create_app
from httpx import AsyncClient, ASGITransport

async def check():
    store = ConfigStore('/tmp/open3e_plan2_check.db')
    await store.initialize()
    app = create_app(store)
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url='http://test') as c:
        for path in ['/', '/settings', '/datapoints', '/write', '/depict', '/system']:
            r = await c.get(path)
            print(f'{path}: {r.status_code}')
            assert r.status_code == 200
    await store.close()
    import os; os.remove('/tmp/open3e_plan2_check.db')

asyncio.run(check())
print('All pages OK')
"
```

- [ ] **Step 3: Commit any remaining changes**

---

## Summary

After completing Plan 2, you have:

- **CAN Engine** with priority-based polling (High/Medium/Low/Off) running in a background thread
- **WebSocket** endpoint at `/ws` with per-client DID subscriptions and auto-reconnect
- **Dashboard** with live-updating value cards and uPlot time-series charts (30 min rolling window)
- **Datapoints browser** with search, filter by ECU/priority, inline priority/polling controls, bulk actions
- **Write values page** with confirmation modal and write-through-engine safety
- **System depiction page** with subprocess output streaming via WebSocket
- **System status page** with software versions, CAN bus stats, engine state, ECU list
- Cross-thread data bridge from engine thread to async WebSocket broadcast

**Next:** Plan 3 adds MQTT publisher, HA discovery with smart defaults, authentication middleware, and remaining polish.
