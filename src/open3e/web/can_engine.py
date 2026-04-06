"""CAN engine with priority scheduler and command queue.

This module provides a CanEngine that runs ALL CAN/UDS communication in a
single dedicated background thread.  The web server communicates with it
exclusively through:

  - ``send_command(cmd)``  — web → engine (thread-safe queue)
  - ``on_data(msg)``       — engine → web (callback, never blocks engine)

The existing O3Eclass uses module-level global flags in Open3Ecodecs that are
NOT thread-safe; serialising every access through one thread makes it safe.
"""

from __future__ import annotations

import os
import queue
import subprocess
import threading
from enum import Enum, auto
from typing import Any, Callable, Dict, List, Optional

# ---------------------------------------------------------------------------
# Public constants (also importable by tests)
# ---------------------------------------------------------------------------

CYCLE_LENGTH: int = 12
MEDIUM_INTERVAL: int = 4
LOW_INTERVAL: int = 12
INTER_DID_DELAY: float = 0.02


# ---------------------------------------------------------------------------
# EngineState
# ---------------------------------------------------------------------------

class EngineState(Enum):
    IDLE = auto()
    CONNECTING = auto()
    POLLING = auto()
    PAUSED = auto()
    EXECUTING_COMMAND = auto()


# ---------------------------------------------------------------------------
# CanEngine
# ---------------------------------------------------------------------------

class CanEngine:
    """CAN communication engine that serialises all O3Eclass access.

    Parameters
    ----------
    store:
        ConfigStore reference (used to persist last values, etc.).
    on_data:
        Optional callback ``on_data(msg: dict)`` invoked by the engine
        thread whenever new data or state change messages are available.
        The callback must be non-blocking (the engine will not wait for it).
    """

    # -- class-level constants (also accessible via module) ------------------
    CYCLE_LENGTH = CYCLE_LENGTH
    MEDIUM_INTERVAL = MEDIUM_INTERVAL
    LOW_INTERVAL = LOW_INTERVAL
    INTER_DID_DELAY = INTER_DID_DELAY

    def __init__(self, store, on_data: Optional[Callable[[Dict], None]] = None):
        self._store = store
        self._on_data = on_data

        # Command queue: web → engine
        self._cmd_queue: queue.Queue = queue.Queue()

        # State protected by a lock
        self._state_lock = threading.Lock()
        self._state: EngineState = EngineState.IDLE

        # Runtime data
        self._ecus: Dict[int, Any] = {}           # address → O3Eclass instance
        self._datapoints: Dict[int, Dict] = {}    # dp_id  → datapoint dict
        self._last_values: Dict[str, Any] = {}    # "ecu:did" → last decoded value

        # Engine control
        self._running: bool = False
        self._thread: Optional[threading.Thread] = None
        self._cycle: int = 0

        # Depiction subprocess support
        self._depict_proc: Optional[subprocess.Popen] = None
        self._depict_lock = threading.Lock()
        self._depict_log: list[str] = []
        self._depict_returncode: Optional[int] = None

    # -----------------------------------------------------------------------
    # State property
    # -----------------------------------------------------------------------

    @property
    def state(self) -> EngineState:
        """Return current engine state (thread-safe read)."""
        with self._state_lock:
            return self._state

    def _set_state(self, state: EngineState) -> None:
        """Set engine state and emit an engine_state message."""
        with self._state_lock:
            self._state = state
        self._emit_data({"type": "engine_state", "state": state.name})

    # -----------------------------------------------------------------------
    # Data emission
    # -----------------------------------------------------------------------

    def _emit_data(self, msg: Dict) -> None:
        """Deliver *msg* to the on_data callback (if set)."""
        if self._on_data is not None:
            try:
                self._on_data(msg)
            except Exception:
                # Never let a misbehaving callback crash the engine
                pass

    # -----------------------------------------------------------------------
    # Command queue
    # -----------------------------------------------------------------------

    def send_command(self, cmd: Dict) -> None:
        """Enqueue *cmd* for the engine thread to process (thread-safe)."""
        self._cmd_queue.put(cmd)

    # -----------------------------------------------------------------------
    # Value cache
    # -----------------------------------------------------------------------

    def get_last_value(self, ecu: int, did: int) -> Any:
        """Return the most-recently cached decoded value for *ecu*/*did*."""
        return self._last_values.get(f"{ecu}:{did}")

    # -----------------------------------------------------------------------
    # Priority scheduler
    # -----------------------------------------------------------------------

    def _build_poll_list(self, cycle: int) -> List[Dict]:
        """Return the list of datapoint dicts to poll on *cycle*.

        Priority tiers
        ~~~~~~~~~~~~~~
        3 (high)   — polled every cycle
        2 (medium) — polled every MEDIUM_INTERVAL cycles (cycle % MEDIUM_INTERVAL == 0)
        1 (low)    — polled every LOW_INTERVAL cycles (cycle % LOW_INTERVAL == 0)
        0/disabled — never polled
        """
        poll = []
        include_medium = (cycle % MEDIUM_INTERVAL == 0)
        include_low = (cycle % LOW_INTERVAL == 0)

        for dp in self._datapoints.values():
            if not dp.get("poll_enabled", 1):
                continue
            priority = dp.get("poll_priority", 1)
            if priority == 3:
                poll.append(dp)
            elif priority == 2 and include_medium:
                poll.append(dp)
            elif priority == 1 and include_low:
                poll.append(dp)
            # priority == 0 or unknown → skip

        return poll

    # -----------------------------------------------------------------------
    # Lifecycle: start / stop
    # -----------------------------------------------------------------------

    def start(
        self,
        can_interface: str,
        can_bitrate: int,
        datapoints: Dict[int, Dict],
        ecus: List[Dict],
    ) -> None:
        """Start the engine background thread."""
        if self._running:
            return

        self._running = True
        self._datapoints = dict(datapoints)

        self._thread = threading.Thread(
            target=self._run,
            args=(can_interface, can_bitrate, ecus),
            daemon=True,
            name="CanEngine",
        )
        self._thread.start()

    def stop(self) -> None:
        """Signal the engine to stop and wait for the thread to exit."""
        self._running = False
        self._cmd_queue.put({"type": "stop"})
        if self._thread is not None:
            self._thread.join(timeout=10)
            self._thread = None

    # -----------------------------------------------------------------------
    # Main engine loop
    # -----------------------------------------------------------------------

    def _run(self, can_interface: str, can_bitrate: int, ecus: List[Dict]) -> None:
        """Main engine loop — runs in the background daemon thread."""
        import time

        try:
            self._set_state(EngineState.CONNECTING)
            self._connect_ecus(can_interface, ecus)
            self._set_state(EngineState.POLLING)

            while self._running:
                # Check for pending commands first
                if self._process_commands():
                    break  # stop command received

                if self._state == EngineState.PAUSED:
                    time.sleep(0.1)
                    continue

                # Build the poll list for this cycle
                poll_list = self._build_poll_list(self._cycle)

                for dp in poll_list:
                    if not self._running:
                        break

                    # Check commands between every DID read
                    if self._process_commands():
                        self._cleanup()
                        return

                    if self._state == EngineState.PAUSED:
                        break

                    self._poll_did(dp)
                    time.sleep(INTER_DID_DELAY)

                self._cycle = (self._cycle + 1) % CYCLE_LENGTH

        except Exception as exc:
            self._emit_data({"type": "engine_error", "error": str(exc)})
        finally:
            self._cleanup()
            self._set_state(EngineState.IDLE)

    def _connect_ecus(self, can_interface: str, ecus: List[Dict]) -> None:
        """Instantiate O3Eclass for each ECU in *ecus*."""
        from open3e.Open3Eclass import O3Eclass

        for ecu in ecus:
            address = ecu["address"]
            dev = ecu.get("device_prop") or None
            try:
                o3e = O3Eclass(
                    ecutx=address,
                    can=can_interface,
                    dev=dev,
                )
                self._ecus[address] = o3e
                self._emit_data({"type": "ecu_connected", "ecu": address})
            except Exception as exc:
                self._emit_data({
                    "type": "ecu_error",
                    "ecu": address,
                    "error": str(exc),
                })

    def _poll_did(self, dp: Dict) -> None:
        """Read a single DID from its ECU and cache/emit the result."""
        ecu_addr = dp["ecu_address"]
        did = dp["did"]

        o3e = self._ecus.get(ecu_addr)
        if o3e is None:
            return

        try:
            value, idstr, _ = o3e.readByDid(did, raw=False)
            cache_key = f"{ecu_addr}:{did}"
            self._last_values[cache_key] = value
            self._emit_data({
                "type": "did_value",
                "ecu": ecu_addr,
                "did": did,
                "name": dp.get("name", idstr),
                "value": value,
            })
        except Exception as exc:
            self._emit_data({
                "type": "did_error",
                "ecu": ecu_addr,
                "did": did,
                "error": str(exc),
            })

    # -----------------------------------------------------------------------
    # Command processing
    # -----------------------------------------------------------------------

    def _process_commands(self) -> bool:
        """Drain pending commands.  Returns True if a *stop* was received."""
        while True:
            try:
                cmd = self._cmd_queue.get_nowait()
            except queue.Empty:
                return False

            cmd_type = cmd.get("type")

            if cmd_type == "stop":
                return True
            elif cmd_type == "pause":
                self._set_state(EngineState.PAUSED)
            elif cmd_type == "resume":
                if self._state == EngineState.PAUSED:
                    self._set_state(EngineState.POLLING)
            elif cmd_type == "read_did":
                self._handle_read(cmd)
            elif cmd_type == "write_did":
                self._handle_write(cmd)
            elif cmd_type == "update_schedule":
                self._handle_update_schedule(cmd)

        # unreachable, but keeps linters happy
        return False  # pragma: no cover

    def _handle_read(self, cmd: Dict) -> None:
        """Execute an on-demand single DID read."""
        prev_state = self.state
        self._set_state(EngineState.EXECUTING_COMMAND)

        ecu_addr = cmd.get("ecu")
        did = cmd.get("did")
        o3e = self._ecus.get(ecu_addr)

        if o3e is None:
            self._emit_data({"type": "cmd_error", "cmd": cmd, "error": "ECU not connected"})
        else:
            try:
                value, idstr, _ = o3e.readByDid(did, raw=cmd.get("raw", False))
                self._last_values[f"{ecu_addr}:{did}"] = value
                self._emit_data({
                    "type": "did_value",
                    "ecu": ecu_addr,
                    "did": did,
                    "name": idstr,
                    "value": value,
                    "on_demand": True,
                })
            except Exception as exc:
                self._emit_data({"type": "cmd_error", "cmd": cmd, "error": str(exc)})

        self._set_state(prev_state)

    def _handle_write(self, cmd: Dict) -> None:
        """Execute a DID write via O3Eclass.writeByDid."""
        prev_state = self.state
        self._set_state(EngineState.EXECUTING_COMMAND)

        ecu_addr = cmd.get("ecu")
        did = cmd.get("did")
        val = cmd.get("value")
        raw = cmd.get("raw", False)
        o3e = self._ecus.get(ecu_addr)

        if o3e is None:
            self._emit_data({"type": "cmd_error", "cmd": cmd, "error": "ECU not connected"})
        else:
            try:
                succ, code = o3e.writeByDid(did, val, raw)
                self._emit_data({
                    "type": "write_result",
                    "ecu": ecu_addr,
                    "did": did,
                    "success": succ,
                    "code": code,
                })
            except Exception as exc:
                self._emit_data({"type": "cmd_error", "cmd": cmd, "error": str(exc)})

        self._set_state(prev_state)

    def _handle_update_schedule(self, cmd: Dict) -> None:
        """Replace the datapoints configuration (update polling schedule)."""
        new_datapoints = cmd.get("datapoints", {})
        self._datapoints = dict(new_datapoints)
        self._emit_data({"type": "schedule_updated", "count": len(self._datapoints)})

    # -----------------------------------------------------------------------
    # Cleanup
    # -----------------------------------------------------------------------

    def _cleanup(self) -> None:
        """Close all open ECU connections."""
        for address, o3e in list(self._ecus.items()):
            try:
                o3e.close()
            except Exception:
                pass
        self._ecus.clear()

    # -----------------------------------------------------------------------
    # Depiction support
    # -----------------------------------------------------------------------

    def start_depiction(self, can_interface: str, on_line: Optional[Callable[[str], None]] = None) -> None:
        """Run ``open3e_depictSystem`` as a subprocess.

        Reads stdout in a dedicated reader thread.  Emits:

        - ``depict_progress`` — for each output line
        - ``depict_complete`` — when the process exits
        """
        with self._depict_lock:
            if self._depict_proc is not None and self._depict_proc.poll() is None:
                # Already running
                return

            try:
                # Use sys.executable to ensure we run within the same venv
                # -u forces unbuffered stdout so lines stream in real time
                import sys as _sys
                env = dict(os.environ, PYTHONUNBUFFERED="1")
                proc = subprocess.Popen(
                    [_sys.executable, "-u", "-m", "open3e.Open3E_depictSystem", "-c", can_interface],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                    env=env,
                )
                self._depict_proc = proc
            except Exception as exc:
                self._emit_data({"type": "depict_error", "error": str(exc)})
                return

        # Server-side log buffer for page refresh persistence
        self._depict_log: list[str] = []
        self._depict_returncode: Optional[int] = None

        def _reader():
            assert proc.stdout is not None
            for line in proc.stdout:
                stripped = line.rstrip("\n")
                self._depict_log.append(stripped)
                if on_line is not None:
                    on_line(stripped)
                self._emit_data({"type": "depict_progress", "line": stripped})
            proc.wait()
            self._depict_returncode = proc.returncode
            with self._depict_lock:
                self._depict_proc = None
            self._emit_data({"type": "depict_complete", "returncode": proc.returncode})

        reader_thread = threading.Thread(target=_reader, daemon=True, name="DepictReader")
        reader_thread.start()

    @property
    def depict_running(self) -> bool:
        """Return True if a depiction subprocess is currently running."""
        with self._depict_lock:
            return self._depict_proc is not None and self._depict_proc.poll() is None

    def get_depict_state(self) -> dict:
        """Return current depiction state including log buffer for page refresh."""
        return {
            "running": self.depict_running,
            "log": getattr(self, "_depict_log", []),
            "returncode": getattr(self, "_depict_returncode", None),
        }

    # -----------------------------------------------------------------------
    # Status
    # -----------------------------------------------------------------------

    def get_status(self) -> Dict:
        """Return a snapshot of engine status."""
        return {
            "state": self.state.name,
            "cycle": self._cycle,
            "ecus_connected": len(self._ecus),
            "datapoints_configured": len(self._datapoints),
            "depict_running": self.depict_running,
        }
