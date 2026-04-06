# open3e Web UI — Design Specification

**Date:** 2026-04-06
**Status:** Approved

## Overview

A web-based management interface for open3e that replaces CLI-only configuration with a modern browser UI. The user launches a single Python command (`open3e-web`) with no arguments. All configuration — CAN interface, MQTT broker, Home Assistant discovery, datapoint polling — is done through the web interface and persisted in SQLite.

## Requirements

1. **Unified launcher** — single Python entry point, no CLI args needed
2. **CAN interface discovery & configuration** — auto-detect interfaces, simple + advanced parameter control
3. **System depiction** — trigger ECU/DID scan from web UI, show live progress
4. **Live data dashboard** — real-time display of datapoint values via WebSocket, time-series charts (rolling 30 min in browser memory)
5. **Datapoint browser** — list all found datapoints with codec info, search/filter, priority assignment
6. **Write values** — set Viessmann system parameters from the web UI with confirmation dialogs
7. **MQTT broker configuration** — host, port, username, password, TLS on/off, CA cert upload
8. **MQTT channel mapping** — per-datapoint MQTT publish enable, custom topics, JSON/split mode
9. **Home Assistant MQTT discovery** — smart defaults from codec metadata + per-datapoint override (entity type, device class, unit, icon)
10. **HA command handling** — writable entities in HA route writes through the CAN engine
11. **Software & CAN bus status** — versions, uptime, CAN error counters, engine state
12. **Priority-based datapoint polling** — High/Medium/Low/Off tiers with weighted interleaved scheduling
13. **Settings persistence** — SQLite database
14. **Optional authentication** — password protection toggle, disabled by default
15. **Database backup/restore** — create, download, upload, restore, delete backups via web UI
16. **Modern UI with graphs** — Bootstrap 5 dark theme, uPlot time-series charts

## Architecture

### Approach: Internal Message Bus

Two components in one process communicating via async queues. The CAN Engine runs in a dedicated background thread and owns all CAN/UDS communication. The Web Server (FastAPI) handles HTTP/WebSocket and talks to the CAN Engine via command/data queues.

```
┌──────────────────────────────────────────────────────────────┐
│                       One Python Process                      │
│                                                                │
│  ┌───────────┐    async Queue     ┌──────────────┐            │
│  │  FastAPI   │ ◄───────────────► │  CAN Engine   │            │
│  │  Server    │  commands / data  │  (thread)     │            │
│  │           │                   │               │            │
│  │  REST     │                   │  Priority     │            │
│  │  WS       │                   │  Scheduler    │            │
│  └─────┬─────┘                   └───────┬───────┘            │
│        │                                 │                    │
│        │                          ┌──────┴───────┐            │
│        │                          │  O3Eclass    │            │
│        │                          │  (existing)  │            │
│        │                          └──────┬───────┘            │
│        │                                 │                    │
│  ┌─────┴───────────┐              ┌──────┴───────┐            │
│  │  Config Store   │              │  SocketCAN   │            │
│  │  (SQLite)       │              └──────────────┘            │
│  └─────────────────┘                                          │
│        │                                                      │
│  ┌─────┴───────────┐                                          │
│  │ MQTT Publisher  │ ──────► MQTT Broker ──────► HA           │
│  └─────────────────┘                                          │
└──────────────────────────────────────────────────────────────┘
```

### Thread Safety Constraint

The existing `Open3Ecodecs.py` uses module-level global flags (`flag_rawmode`, `flag_binary`). These are not thread-safe. **All CAN/codec access MUST be serialized through the CAN Engine thread.** The web server NEVER calls `O3Eclass` methods directly — it sends commands via the async queue and receives results via the data queue.

### Existing Code Policy

The existing open3e source files are not modified. The web module imports `O3Eclass`, codec classes, and datapoint definitions as a library. The original CLI commands (`open3e`, `open3e_depictSystem`, `open3e_dids2json`) continue to work independently.

## Module Structure

```
src/open3e/
├── __init__.py                (existing)
├── Open3Eclient.py            (existing — untouched)
├── Open3Eclass.py             (existing — used by CAN engine)
├── Open3Ecodecs.py            (existing — used as-is)
├── Open3Edatapoints.py        (existing — used as-is)
├── ...                        (all existing files untouched)
│
├── web/                       NEW — all web UI code
│   ├── __init__.py
│   ├── launcher.py            Entry point: discover CAN, init DB, start all
│   ├── can_engine.py          CAN/UDS communication + priority scheduler
│   ├── server.py              FastAPI app, REST routes, WebSocket
│   ├── config_store.py        SQLite abstraction for all settings
│   ├── mqtt_publisher.py      MQTT client, publish loop, HA command listener
│   ├── ha_discovery.py        HA entity type inference, discovery payloads
│   ├── can_discovery.py       Detect available CAN interfaces on the OS
│   ├── auth.py                Optional password middleware (scrypt hashing)
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   └── templates/
│       ├── base.html          Layout shell (sidebar nav, status bar, dark theme)
│       ├── dashboard.html     Live data + charts
│       ├── datapoints.html    Browse/search all DIDs
│       ├── write.html         Write values to writable DIDs
│       ├── settings.html      CAN, MQTT, HA, system settings (tabbed)
│       ├── system.html        Status, CAN bus info, versions
│       ├── depict.html        Trigger system scan, show progress
│       └── login.html         Password form (shown when auth enabled)
```

## Database Schema (SQLite)

Schema version tracked via `PRAGMA user_version`.

```sql
-- General application settings (key-value)
CREATE TABLE settings (
    key   TEXT PRIMARY KEY,
    value TEXT
);

-- Discovered ECUs from system depiction
CREATE TABLE ecus (
    address     INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    device_prop TEXT,
    dp_list     TEXT,
    last_seen   TIMESTAMP
);

-- Datapoints per ECU
CREATE TABLE datapoints (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    ecu_address   INTEGER NOT NULL REFERENCES ecus(address),
    did           INTEGER NOT NULL,
    name          TEXT NOT NULL,
    codec_type    TEXT,
    data_length   INTEGER,
    is_writable   BOOLEAN DEFAULT 0,
    poll_priority INTEGER DEFAULT 1,
    poll_enabled  BOOLEAN DEFAULT 1,
    UNIQUE(ecu_address, did)
);

-- HA discovery configuration per datapoint sub-field
CREATE TABLE ha_entities (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    datapoint_id    INTEGER NOT NULL REFERENCES datapoints(id),
    sub_field       TEXT,
    enabled         BOOLEAN DEFAULT 0,
    ha_component    TEXT NOT NULL,
    device_class    TEXT,
    unit            TEXT,
    icon            TEXT,
    entity_name     TEXT,
    UNIQUE(datapoint_id, sub_field)
);

-- MQTT topic mapping per datapoint
CREATE TABLE mqtt_mappings (
    datapoint_id    INTEGER PRIMARY KEY REFERENCES datapoints(id),
    enabled         BOOLEAN DEFAULT 1,
    custom_topic    TEXT,
    publish_json    BOOLEAN DEFAULT 1
);
```

### Settings Keys

CAN: `can_interface`, `can_bitrate`, `can_advanced_params` (JSON)

MQTT: `mqtt_host`, `mqtt_port`, `mqtt_user`, `mqtt_password`, `mqtt_tls_enabled`, `mqtt_ca_cert` (base64 PEM), `mqtt_topic_prefix`, `mqtt_format_string`, `mqtt_client_id`

HA: `ha_discovery_enabled`, `ha_discovery_prefix`

Auth: `auth_enabled`, `auth_password_hash`

System: `web_port`, `polling_default_priority`, `depiction_status`, `depiction_timestamp`

### Database Backup

- **Create:** `POST /api/backup` — uses `VACUUM INTO` for atomic consistent copy. Stored in `backups/` directory next to the database.
- **List:** `GET /api/backups` — scans `backups/` directory, returns filenames with timestamps and sizes.
- **Download:** `GET /api/backup/{filename}` — streams file to browser.
- **Restore:** `POST /api/backup/restore` — upload `.db` file, stop engine, replace DB, run schema migrations if needed, restart engine.
- **Delete:** `DELETE /api/backup/{filename}` — removes backup file.
- **Security:** Backup filenames are validated server-side (alphanumeric, dashes, underscores, `.db` extension only). Path separators and `..` are rejected to prevent path traversal.

## Priority Scheduler

### Poll Tiers

| Priority | Label  | Frequency       | Typical datapoints                              |
|----------|--------|----------------|------------------------------------------------|
| 3        | High   | Every cycle    | FlowTemp, ReturnTemp, OutsideTemp, Compressor  |
| 2        | Medium | Every 4th cycle| WaterPressure, DHW, EnergyCounters              |
| 1        | Low    | Every 12th     | SoftwareVersion, SerialNumber, ErrorHistory     |
| 0        | Off    | Never          | User-disabled datapoints                        |

### Cycle Pattern (12-cycle rotation)

```
cycle  0: high + medium + low
cycle  1: high
cycle  2: high
cycle  3: high + medium
cycle  4: high
cycle  5: high
cycle  6: high + medium
cycle  7: high
cycle  8: high
cycle  9: high + medium
cycle 10: high
cycle 11: high
```

20ms delay between each UDS request. Command queue checked between every DID read for immediate responsiveness to user actions.

### Engine States

```
IDLE → CONNECTING → POLLING ⇄ PAUSED
                      ↕
                 EXECUTING_COMMAND
```

State transitions are pushed to all WebSocket clients.

## MQTT Publisher

- Subscribes to data events from CAN engine output queue
- Checks per-datapoint `mqtt_mappings` before publishing
- Uses global `mqtt_format_string` or per-datapoint `custom_topic`
- Publishes as JSON or splits complex types into scalar sub-topics
- Manages LWT (`online`/`offline`) on topic prefix
- Reconfigurable live — settings changes trigger disconnect/reconnect
- TLS: reads base64 CA cert from settings, writes to temp file, passes to `tls_set()`

## Home Assistant MQTT Discovery

### Discovery Message Format

Published to `{ha_prefix}/{component}/{node_id}/{object_id}/config`:

```json
{
  "name": "Flow Temperature",
  "unique_id": "open3e_680_268_actual",
  "state_topic": "open3e/FlowTemperatureSensor/Actual",
  "device_class": "temperature",
  "unit_of_measurement": "°C",
  "icon": "mdi:thermometer",
  "device": {
    "identifiers": ["open3e_680"],
    "name": "Vitocal (0x680)",
    "manufacturer": "Viessmann",
    "model": "HPMUMASTER",
    "sw_version": "3.45.0",
    "via_device": "open3e"
  }
}
```

- One HA device per ECU
- `unique_id`: `open3e_{ecu}_{did}_{subfield}` — deterministic, survives restarts
- Published at startup for all enabled entities, and on config changes
- Disabling an entity publishes empty payload to remove it from HA
- Writable entities include `command_topic` — MQTT publisher listens and routes writes through CAN engine queue

### Smart Defaults Inference

```python
INFERENCE_RULES = [
    # (name_pattern,      codec_type,     component,       device_class,  unit,  icon)
    ("*Temperature*",     "O3EInt16",     "sensor",        "temperature", "°C",  "mdi:thermometer"),
    ("*Pressure*",        "O3EInt16",     "sensor",        "pressure",    "bar", "mdi:gauge"),
    ("*Energy*",          "O3EInt32",     "sensor",        "energy",      "kWh", "mdi:lightning-bolt"),
    ("*FlowMeter*",       "O3EInt32",     "sensor",        "water",       "L",   "mdi:water"),
    ("*Power*",           "O3EInt16",     "sensor",        "power",       "W",   "mdi:flash"),
    ("*OperationMode*",   "O3EEnum",      "select",        None,          None,  "mdi:cog"),
    ("*OperationState*",  "O3EEnum",      "select",        None,          None,  "mdi:toggle-switch"),
    ("*Setpoint*",        "O3EInt16",     "number",        "temperature", "°C",  "mdi:thermostat"),
    ("*Pump*",            "O3EBool",      "binary_sensor",  None,          None,  "mdi:pump"),
]
```

For `O3EComplexType` DIDs: smart defaults create an entity ONLY for the `Actual` sub-field. User can enable additional sub-fields manually.

Entities default to `enabled = false`. User explicitly enables via web UI.

## Web UI Pages

### Technology Stack
- **Backend:** FastAPI + Jinja2 templates + uvicorn
- **Frontend:** Bootstrap 5.3 (CDN, dark theme), uPlot (time-series charts), vanilla JS + htmx
- **Real-time:** WebSocket at `/ws`

### Layout
Sidebar navigation, persistent across all pages. Top bar shows connection status indicators (CAN, MQTT, Engine state with color-coded dots).

### Dashboard
- Grid of cards, one per pinned datapoint: current value, unit, sparkline
- Click card → full-width uPlot chart (rolling 30 min window in browser memory)
- Overlay multiple datapoints on one chart
- Auto-updates via WebSocket

### Datapoints
- Searchable, filterable table of all discovered DIDs
- Columns: ECU, DID#, Name, Codec Type, Current Value, Priority, Poll Enabled, HA Enabled, MQTT Enabled
- Inline controls: priority dropdown, toggle switches
- Row click → detail panel with sub-fields, raw hex, codec info
- Bulk actions: select multiple → set priority, enable/disable
- "Pin to Dashboard" button per datapoint

### Write Values
- Only writable datapoints (from `Open3Edatapoints_writables.json`)
- Current value display + input field + Write button
- Enum types: dropdown from `Open3Eenums`
- Complex types: individual input per sub-field
- Confirmation dialog before every write
- Success/error toast notification

### Settings (tabbed)

**CAN tab:** Auto-detected interfaces as radio buttons, manual entry fallback, bitrate, "Advanced" collapsible (restart-ms, listen-only, loopback, tx queue len, sample point, SJW). Apply & Connect button.

**MQTT tab:** Host, port, user, password, TLS toggle + CA cert upload, topic prefix, format string with live preview, client ID. Test Connection + Save & Reconnect buttons.

**Home Assistant tab:** Global enable toggle, discovery prefix, entity table with inline edit, "Apply suggested defaults" button, bulk enable/disable.

**System tab:** Database backup section (create, list, download, restore, delete). Authentication enable/disable + password. Web server port.

### System Status
- Software: open3e version, web UI version, Python version, uptime
- CAN bus: interface, state, bitrate, RX/TX counts, error counters
- Engine: state, cycle count, datapoints polled, avg cycle time
- MQTT: connection state, messages published, last publish time
- ECU list: address, name, device property, DID count, last read

### System Depiction
- "Start Scan" button (prompts to pause engine if polling)
- Live output console streamed via WebSocket from subprocess stdout
- On completion: summary, "Load into configuration" button
- Populates ecus + datapoints tables, applies smart defaults

### Login
- Single password field (shown only when auth is enabled)
- Session cookie with random token, 24h idle timeout

## WebSocket Protocol

Endpoint: `/ws`

### Server → Client
```json
{"type": "did_value", "ecu": 1664, "did": 268, "name": "FlowTemperatureSensor", "value": {}, "ts": 1712345678}
{"type": "engine_state", "state": "polling", "cycle": 42}
{"type": "can_status", "interface": "can0", "state": "up", "errors": 0}
{"type": "mqtt_status", "connected": true}
{"type": "depict_progress", "line": "found 268:9:FlowTemperatureSensor"}
```

### Client → Server
```json
{"type": "subscribe", "dids": [268, 269, 274]}
{"type": "subscribe", "dids": "*"}
{"type": "write", "ecu": 1664, "did": 396, "value": 48.0}
```

Subscribe mechanism prevents flooding: browser only receives updates for subscribed DIDs.

## REST API

```
GET    /api/ecus                        List discovered ECUs
GET    /api/datapoints?ecu=&priority=   List datapoints (filtered)
PATCH  /api/datapoints/{id}             Update priority, poll_enabled
GET    /api/datapoints/{id}/value       Last known value

POST   /api/write                       Write a value to a DID
POST   /api/depict/start                Start system depiction
GET    /api/depict/status               Depiction subprocess state

GET    /api/settings                    All settings
PATCH  /api/settings                    Update settings
POST   /api/settings/test-mqtt          Test MQTT connection

GET    /api/ha/entities                 List HA entity configs
PATCH  /api/ha/entities/{id}            Update HA entity config
POST   /api/ha/apply-defaults           Apply smart defaults

GET    /api/mqtt/mappings               List MQTT mappings
PATCH  /api/mqtt/mappings/{id}          Update mapping

POST   /api/backup                      Create backup
GET    /api/backups                     List backups
GET    /api/backup/{filename}           Download backup file
POST   /api/backup/restore              Upload & restore backup
DELETE /api/backup/{filename}           Delete backup

GET    /api/status                      System status
GET    /api/can/interfaces              Discover available CAN interfaces

POST   /api/auth/login                  Authenticate
POST   /api/auth/logout                 Clear session
PATCH  /api/auth/settings               Enable/disable auth, change password
```

## Launcher & First-Run Experience

### Entry Point

```
open3e-web = "open3e.web.launcher:main"
```

### Startup Sequence

1. Init SQLite database (create tables if not exist, run migrations)
2. Discover CAN interfaces (best-effort, empty list on non-Linux)
3. Load settings from DB
4. If CAN interface configured and available: start CAN engine thread + MQTT publisher
5. Start FastAPI/uvicorn on configured port (default 8080, fallback 8081+)
6. Print URL to stdout

### First-Run Flow

1. User runs `open3e-web` → terminal prints URL
2. Browser → Dashboard (empty, amber status indicators)
3. Settings → CAN tab → select interface → Apply
4. System Depiction → Start Scan → live progress → complete
5. Dashboard populates with live data
6. Settings → MQTT tab → configure broker → Test → Save
7. Settings → HA tab → enable discovery → select datapoints → apply

After first run, everything auto-starts on next launch.

## Dependencies

New dependencies (added as optional `web` extra):

```toml
[project.optional-dependencies]
web = [
    "fastapi>=0.110",
    "uvicorn[standard]>=0.29",
    "jinja2>=3.1",
    "aiosqlite>=0.20",
    "python-multipart>=0.0.9",
]
```

## Platform Notes

- **Linux (Raspberry Pi):** Full functionality. CAN interface discovery via `/sys/class/net/*/type` and `ip link`.
- **macOS / Windows:** CAN discovery returns empty list. Manual interface entry available. Useful for development and testing the web UI without hardware.

## Future Extensions (Out of Scope)

- **DoIP support** — the existing open3e codebase supports DoIP (TCP/IP to CAN gateway). Adding a DoIP connection option to the CAN settings tab is a natural extension but not part of the initial implementation.
- **Persistent historical data** — storing time-series data in SQLite for long-term charting (currently browser-only rolling window).
- **Multi-user authentication** — roles, permissions, audit log.
- **Firmware update management** — triggering firmware updates on connected ECUs.
