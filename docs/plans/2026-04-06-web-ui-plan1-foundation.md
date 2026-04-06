# Web UI Plan 1: Foundation & Configuration

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish a working FastAPI web server with settings pages for CAN, MQTT, and HA configuration — persistent in SQLite — launchable with a single `open3e-web` command.

**Architecture:** FastAPI serves Jinja2 templates with a Bootstrap 5 dark theme. All settings are stored in SQLite via a `ConfigStore` abstraction. CAN interface discovery scans `/sys/class/net/` on Linux, gracefully degrades on other platforms. The launcher wires everything together and starts uvicorn.

**Tech Stack:** Python 3.9+, FastAPI, uvicorn, Jinja2, aiosqlite, Bootstrap 5.3 (CDN), htmx (CDN)

**Spec reference:** `docs/specs/2026-04-06-web-ui-design.md`

---

## File Map

```
src/open3e/web/
├── __init__.py              Package init
├── launcher.py              Entry point: init DB, discover CAN, start uvicorn
├── config_store.py          SQLite wrapper: settings, ecus, datapoints, ha, mqtt
├── can_discovery.py         Detect CAN interfaces on the OS
├── server.py                FastAPI app: routes, template rendering, static mount
├── auth.py                  Optional password middleware (stub — full impl in Plan 3)
├── static/
│   ├── css/
│   │   └── app.css          Custom styles on top of Bootstrap
│   └── js/
│       └── app.js           htmx helpers, toast notifications, settings tabs
└── templates/
    ├── base.html            Layout shell: sidebar, status bar, dark theme
    ├── dashboard.html       Placeholder dashboard (populated in Plan 2)
    ├── settings.html        CAN / MQTT / HA / System tabs
    └── login.html           Password form (stub — full impl in Plan 3)

tests/
└── web/
    ├── __init__.py
    ├── test_config_store.py
    ├── test_can_discovery.py
    └── test_server.py
```

---

### Task 1: Project scaffolding

**Files:**
- Create: `src/open3e/web/__init__.py`
- Create: `src/open3e/web/static/css/app.css`
- Create: `src/open3e/web/static/js/app.js`
- Create: `tests/web/__init__.py`
- Modify: `pyproject.toml`

- [ ] **Step 1: Create the web package directory structure**

```bash
mkdir -p src/open3e/web/static/css
mkdir -p src/open3e/web/static/js
mkdir -p src/open3e/web/templates
mkdir -p tests/web
```

- [ ] **Step 2: Create package init files**

`src/open3e/web/__init__.py`:
```python
"""open3e web UI — browser-based management interface."""
```

`tests/web/__init__.py`:
```python
```

- [ ] **Step 3: Create placeholder static files**

`src/open3e/web/static/css/app.css`:
```css
/* open3e web UI — custom styles on top of Bootstrap 5.3 dark theme */

:root {
    --sidebar-width: 240px;
    --status-bar-height: 48px;
}

body {
    min-height: 100vh;
}

/* Sidebar navigation */
.sidebar {
    position: fixed;
    top: 0;
    left: 0;
    width: var(--sidebar-width);
    height: 100vh;
    padding: 1rem;
    background-color: var(--bs-dark);
    border-right: 1px solid var(--bs-border-color);
    overflow-y: auto;
    z-index: 1000;
}

.sidebar .nav-link {
    color: var(--bs-gray-400);
    border-radius: 0.375rem;
    padding: 0.5rem 0.75rem;
    margin-bottom: 0.125rem;
}

.sidebar .nav-link:hover {
    color: var(--bs-white);
    background-color: var(--bs-gray-800);
}

.sidebar .nav-link.active {
    color: var(--bs-white);
    background-color: var(--bs-primary);
}

/* Main content area */
.main-content {
    margin-left: var(--sidebar-width);
    padding: 1rem 1.5rem;
    min-height: 100vh;
}

/* Status bar in sidebar footer */
.status-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    width: var(--sidebar-width);
    padding: 0.5rem 1rem;
    background-color: var(--bs-dark);
    border-top: 1px solid var(--bs-border-color);
    border-right: 1px solid var(--bs-border-color);
    font-size: 0.75rem;
}

.status-dot {
    display: inline-block;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    margin-right: 4px;
}

.status-dot.green { background-color: var(--bs-success); }
.status-dot.red { background-color: var(--bs-danger); }
.status-dot.amber { background-color: var(--bs-warning); }
.status-dot.gray { background-color: var(--bs-gray-600); }

/* Toast container */
.toast-container {
    position: fixed;
    top: 1rem;
    right: 1rem;
    z-index: 2000;
}

/* Settings tabs */
.settings-content .tab-pane {
    padding-top: 1.5rem;
}

/* Responsive: collapse sidebar on small screens */
@media (max-width: 768px) {
    .sidebar {
        width: 100%;
        height: auto;
        position: relative;
        border-right: none;
        border-bottom: 1px solid var(--bs-border-color);
    }
    .main-content {
        margin-left: 0;
    }
    .status-bar {
        width: 100%;
        position: relative;
        border-right: none;
    }
}
```

`src/open3e/web/static/js/app.js`:
```javascript
/* open3e web UI — shared JavaScript utilities */

/**
 * Show a Bootstrap toast notification.
 * @param {string} message - Text to display
 * @param {string} type - "success", "danger", "warning", "info"
 */
function showToast(message, type = "info") {
    const container = document.getElementById("toast-container");
    if (!container) return;

    const id = "toast-" + Date.now();
    const html = `
        <div id="${id}" class="toast align-items-center text-bg-${type} border-0" role="alert">
            <div class="d-flex">
                <div class="toast-body">${message}</div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto"
                        data-bs-dismiss="toast"></button>
            </div>
        </div>`;
    container.insertAdjacentHTML("beforeend", html);

    const el = document.getElementById(id);
    const toast = new bootstrap.Toast(el, { delay: 4000 });
    toast.show();
    el.addEventListener("hidden.bs.toast", () => el.remove());
}

/**
 * Send a PATCH/POST request with JSON body and show result toast.
 * @param {string} url
 * @param {string} method - "PATCH", "POST", "DELETE"
 * @param {object} body
 * @returns {Promise<object>} parsed JSON response
 */
async function apiCall(url, method, body = null) {
    const opts = {
        method: method,
        headers: { "Content-Type": "application/json" },
    };
    if (body !== null) {
        opts.body = JSON.stringify(body);
    }
    const resp = await fetch(url, opts);
    const data = await resp.json();
    if (!resp.ok) {
        showToast(data.detail || "Request failed", "danger");
        throw new Error(data.detail || resp.statusText);
    }
    return data;
}
```

- [ ] **Step 4: Update pyproject.toml with web dependencies and entry point**

Add to `pyproject.toml` after the existing `[project.optional-dependencies]` section:

```toml
[project.optional-dependencies]
dev = ["pytest", "pytest-cov", "black==21.10b0"]
web = [
    "fastapi>=0.110",
    "uvicorn[standard]>=0.29",
    "jinja2>=3.1",
    "aiosqlite>=0.20",
    "python-multipart>=0.0.9",
]
```

Add to `[project.scripts]` section:

```toml
[project.scripts]
open3e = "open3e.Open3Eclient:main"
open3e_depictSystem = "open3e.Open3E_depictSystem:main"
open3e_dids2json = "open3e.Open3E_dids2json:main"
open3e-web = "open3e.web.launcher:main"
```

- [ ] **Step 5: Install in editable mode with web extras**

```bash
pip install --editable ".[web,dev]"
```

- [ ] **Step 6: Commit**

```bash
git add src/open3e/web/ tests/web/ pyproject.toml
git commit -m "Scaffold web UI package with static assets and dependencies"
```

---

### Task 2: Config Store — SQLite database layer

**Files:**
- Create: `src/open3e/web/config_store.py`
- Create: `tests/web/test_config_store.py`

- [ ] **Step 1: Write failing tests for ConfigStore**

`tests/web/test_config_store.py`:
```python
import os
import pytest
import asyncio
from pathlib import Path

from open3e.web.config_store import ConfigStore

TEST_DB = "/tmp/open3e_test.db"


@pytest.fixture
def store():
    """Create a fresh ConfigStore for each test."""
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    s = ConfigStore(TEST_DB)
    asyncio.get_event_loop().run_until_complete(s.initialize())
    yield s
    asyncio.get_event_loop().run_until_complete(s.close())
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)


@pytest.fixture
def event_loop():
    """Provide a fresh event loop for async tests."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


def run(coro):
    """Helper to run async code in sync tests."""
    return asyncio.get_event_loop().run_until_complete(coro)


class TestSettings:
    def test_get_unset_returns_none(self, store):
        assert run(store.get_setting("nonexistent")) is None

    def test_get_unset_returns_default(self, store):
        assert run(store.get_setting("nonexistent", "fallback")) == "fallback"

    def test_set_and_get(self, store):
        run(store.set_setting("mqtt_host", "192.168.1.1"))
        assert run(store.get_setting("mqtt_host")) == "192.168.1.1"

    def test_overwrite(self, store):
        run(store.set_setting("mqtt_host", "old"))
        run(store.set_setting("mqtt_host", "new"))
        assert run(store.get_setting("mqtt_host")) == "new"

    def test_get_all_settings(self, store):
        run(store.set_setting("a", "1"))
        run(store.set_setting("b", "2"))
        settings = run(store.get_all_settings())
        assert settings == {"a": "1", "b": "2"}


class TestEcus:
    def test_upsert_and_get(self, store):
        run(store.upsert_ecu(0x680, "vitocal", "HPMUMASTER", "Open3Edatapoints_680.py"))
        ecus = run(store.get_ecus())
        assert len(ecus) == 1
        assert ecus[0]["address"] == 0x680
        assert ecus[0]["name"] == "vitocal"

    def test_upsert_overwrites(self, store):
        run(store.upsert_ecu(0x680, "old", "HPMUMASTER", "dp.py"))
        run(store.upsert_ecu(0x680, "new", "HPMUMASTER", "dp.py"))
        ecus = run(store.get_ecus())
        assert len(ecus) == 1
        assert ecus[0]["name"] == "new"


class TestDatapoints:
    def test_upsert_and_get(self, store):
        run(store.upsert_ecu(0x680, "vitocal", "HPMUMASTER", "dp.py"))
        dp_id = run(store.upsert_datapoint(0x680, 268, "FlowTemperatureSensor", "O3EComplexType", 9, False))
        dps = run(store.get_datapoints(ecu_address=0x680))
        assert len(dps) == 1
        assert dps[0]["did"] == 268
        assert dps[0]["name"] == "FlowTemperatureSensor"
        assert dps[0]["poll_priority"] == 1  # default low

    def test_update_priority(self, store):
        run(store.upsert_ecu(0x680, "vitocal", "HPMUMASTER", "dp.py"))
        dp_id = run(store.upsert_datapoint(0x680, 268, "FlowTemp", "O3EComplexType", 9, False))
        run(store.update_datapoint(dp_id, poll_priority=3))
        dps = run(store.get_datapoints(ecu_address=0x680))
        assert dps[0]["poll_priority"] == 3

    def test_filter_by_priority(self, store):
        run(store.upsert_ecu(0x680, "vitocal", "HPMUMASTER", "dp.py"))
        run(store.upsert_datapoint(0x680, 268, "FlowTemp", "O3EComplexType", 9, False))
        dp_id2 = run(store.upsert_datapoint(0x680, 269, "ReturnTemp", "O3EComplexType", 9, False))
        run(store.update_datapoint(dp_id2, poll_priority=3))
        high = run(store.get_datapoints(poll_priority=3))
        assert len(high) == 1
        assert high[0]["did"] == 269


class TestHaEntities:
    def test_upsert_and_get(self, store):
        run(store.upsert_ecu(0x680, "vitocal", "HPMUMASTER", "dp.py"))
        dp_id = run(store.upsert_datapoint(0x680, 268, "FlowTemp", "O3EComplexType", 9, False))
        run(store.upsert_ha_entity(dp_id, "Actual", "sensor", "temperature", "°C", "mdi:thermometer", "Flow Temperature"))
        entities = run(store.get_ha_entities())
        assert len(entities) == 1
        assert entities[0]["ha_component"] == "sensor"
        assert entities[0]["sub_field"] == "Actual"

    def test_enable_disable(self, store):
        run(store.upsert_ecu(0x680, "vitocal", "HPMUMASTER", "dp.py"))
        dp_id = run(store.upsert_datapoint(0x680, 268, "FlowTemp", "O3EComplexType", 9, False))
        ha_id = run(store.upsert_ha_entity(dp_id, "Actual", "sensor", "temperature", "°C", "mdi:thermometer", "Flow Temp"))
        run(store.update_ha_entity(ha_id, enabled=True))
        enabled = run(store.get_ha_entities(enabled=True))
        assert len(enabled) == 1


class TestMqttMappings:
    def test_upsert_and_get(self, store):
        run(store.upsert_ecu(0x680, "vitocal", "HPMUMASTER", "dp.py"))
        dp_id = run(store.upsert_datapoint(0x680, 268, "FlowTemp", "O3EComplexType", 9, False))
        run(store.upsert_mqtt_mapping(dp_id, enabled=True, custom_topic=None, publish_json=True))
        mappings = run(store.get_mqtt_mappings())
        assert len(mappings) == 1
        assert mappings[0]["enabled"] is True


class TestBackup:
    def test_create_and_list(self, store):
        filename = run(store.create_backup())
        assert filename.endswith(".db")
        backups = run(store.list_backups())
        assert len(backups) == 1
        assert backups[0]["filename"] == filename

    def test_delete(self, store):
        filename = run(store.create_backup())
        run(store.delete_backup(filename))
        backups = run(store.list_backups())
        assert len(backups) == 0

    def test_backup_path(self, store):
        filename = run(store.create_backup())
        path = run(store.get_backup_path(filename))
        assert path.exists()
        assert path.name == filename

    def test_invalid_filename_rejected(self, store):
        with pytest.raises(ValueError):
            run(store.get_backup_path("../etc/passwd"))

    def test_path_traversal_rejected(self, store):
        with pytest.raises(ValueError):
            run(store.get_backup_path("foo/../../bar.db"))


class TestSchemaVersion:
    def test_initial_version(self, store):
        version = run(store.get_schema_version())
        assert version == 1
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/web/test_config_store.py -v
```

Expected: `ModuleNotFoundError: No module named 'open3e.web.config_store'`

- [ ] **Step 3: Implement ConfigStore**

`src/open3e/web/config_store.py`:
```python
"""SQLite-backed configuration store for open3e web UI."""

import os
import re
import aiosqlite
from datetime import datetime
from pathlib import Path
from typing import Optional


SCHEMA_VERSION = 1

# Backup filenames must be safe: alphanumeric, dashes, underscores, ending in .db
_SAFE_FILENAME = re.compile(r"^[a-zA-Z0-9_-]+\.db$")

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS settings (
    key   TEXT PRIMARY KEY,
    value TEXT
);

CREATE TABLE IF NOT EXISTS ecus (
    address     INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    device_prop TEXT,
    dp_list     TEXT,
    last_seen   TIMESTAMP
);

CREATE TABLE IF NOT EXISTS datapoints (
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

CREATE TABLE IF NOT EXISTS ha_entities (
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

CREATE TABLE IF NOT EXISTS mqtt_mappings (
    datapoint_id    INTEGER PRIMARY KEY REFERENCES datapoints(id),
    enabled         BOOLEAN DEFAULT 1,
    custom_topic    TEXT,
    publish_json    BOOLEAN DEFAULT 1
);
"""


def _validate_backup_filename(filename: str) -> None:
    """Reject filenames that could cause path traversal."""
    if not _SAFE_FILENAME.match(filename):
        raise ValueError(f"Invalid backup filename: {filename}")
    if ".." in filename or "/" in filename or "\\" in filename:
        raise ValueError(f"Invalid backup filename: {filename}")


class ConfigStore:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.backup_dir = Path(db_path).parent / "backups"
        self._db: Optional[aiosqlite.Connection] = None

    async def initialize(self) -> None:
        """Open database and create schema if needed."""
        self._db = await aiosqlite.connect(self.db_path)
        self._db.row_factory = aiosqlite.Row
        await self._db.executescript(SCHEMA_SQL)
        # Set schema version if not set
        cursor = await self._db.execute("PRAGMA user_version")
        row = await cursor.fetchone()
        if row[0] == 0:
            await self._db.execute(f"PRAGMA user_version = {SCHEMA_VERSION}")
        await self._db.commit()

    async def close(self) -> None:
        if self._db:
            await self._db.close()
            self._db = None

    # --- Settings ---

    async def get_setting(self, key: str, default: Optional[str] = None) -> Optional[str]:
        cursor = await self._db.execute("SELECT value FROM settings WHERE key = ?", (key,))
        row = await cursor.fetchone()
        return row["value"] if row else default

    async def set_setting(self, key: str, value: str) -> None:
        await self._db.execute(
            "INSERT INTO settings (key, value) VALUES (?, ?) ON CONFLICT(key) DO UPDATE SET value = ?",
            (key, value, value),
        )
        await self._db.commit()

    async def get_all_settings(self) -> dict:
        cursor = await self._db.execute("SELECT key, value FROM settings")
        rows = await cursor.fetchall()
        return {row["key"]: row["value"] for row in rows}

    # --- ECUs ---

    async def upsert_ecu(self, address: int, name: str, device_prop: str, dp_list: str) -> None:
        now = datetime.utcnow().isoformat()
        await self._db.execute(
            """INSERT INTO ecus (address, name, device_prop, dp_list, last_seen)
               VALUES (?, ?, ?, ?, ?)
               ON CONFLICT(address) DO UPDATE SET
                 name = excluded.name,
                 device_prop = excluded.device_prop,
                 dp_list = excluded.dp_list,
                 last_seen = excluded.last_seen""",
            (address, name, device_prop, dp_list, now),
        )
        await self._db.commit()

    async def get_ecus(self) -> list:
        cursor = await self._db.execute("SELECT * FROM ecus ORDER BY address")
        rows = await cursor.fetchall()
        return [dict(row) for row in rows]

    # --- Datapoints ---

    async def upsert_datapoint(
        self, ecu_address: int, did: int, name: str,
        codec_type: str, data_length: int, is_writable: bool
    ) -> int:
        cursor = await self._db.execute(
            """INSERT INTO datapoints (ecu_address, did, name, codec_type, data_length, is_writable)
               VALUES (?, ?, ?, ?, ?, ?)
               ON CONFLICT(ecu_address, did) DO UPDATE SET
                 name = excluded.name,
                 codec_type = excluded.codec_type,
                 data_length = excluded.data_length,
                 is_writable = excluded.is_writable""",
            (ecu_address, did, name, codec_type, data_length, is_writable),
        )
        await self._db.commit()
        return cursor.lastrowid

    async def get_datapoints(
        self,
        ecu_address: Optional[int] = None,
        poll_priority: Optional[int] = None,
        poll_enabled: Optional[bool] = None,
    ) -> list:
        query = "SELECT * FROM datapoints WHERE 1=1"
        params = []
        if ecu_address is not None:
            query += " AND ecu_address = ?"
            params.append(ecu_address)
        if poll_priority is not None:
            query += " AND poll_priority = ?"
            params.append(poll_priority)
        if poll_enabled is not None:
            query += " AND poll_enabled = ?"
            params.append(int(poll_enabled))
        query += " ORDER BY ecu_address, did"
        cursor = await self._db.execute(query, params)
        rows = await cursor.fetchall()
        return [dict(row) for row in rows]

    async def update_datapoint(self, dp_id: int, **kwargs) -> None:
        allowed = {"poll_priority", "poll_enabled", "is_writable"}
        fields = {k: v for k, v in kwargs.items() if k in allowed}
        if not fields:
            return
        set_clause = ", ".join(f"{k} = ?" for k in fields)
        values = list(fields.values()) + [dp_id]
        await self._db.execute(f"UPDATE datapoints SET {set_clause} WHERE id = ?", values)
        await self._db.commit()

    # --- HA Entities ---

    async def upsert_ha_entity(
        self, datapoint_id: int, sub_field: Optional[str],
        ha_component: str, device_class: Optional[str],
        unit: Optional[str], icon: Optional[str],
        entity_name: Optional[str],
    ) -> int:
        cursor = await self._db.execute(
            """INSERT INTO ha_entities (datapoint_id, sub_field, ha_component, device_class, unit, icon, entity_name)
               VALUES (?, ?, ?, ?, ?, ?, ?)
               ON CONFLICT(datapoint_id, sub_field) DO UPDATE SET
                 ha_component = excluded.ha_component,
                 device_class = excluded.device_class,
                 unit = excluded.unit,
                 icon = excluded.icon,
                 entity_name = excluded.entity_name""",
            (datapoint_id, sub_field, ha_component, device_class, unit, icon, entity_name),
        )
        await self._db.commit()
        return cursor.lastrowid

    async def get_ha_entities(self, enabled: Optional[bool] = None) -> list:
        query = """SELECT he.*, dp.ecu_address, dp.did, dp.name as dp_name
                   FROM ha_entities he
                   JOIN datapoints dp ON he.datapoint_id = dp.id
                   WHERE 1=1"""
        params = []
        if enabled is not None:
            query += " AND he.enabled = ?"
            params.append(int(enabled))
        query += " ORDER BY dp.ecu_address, dp.did, he.sub_field"
        cursor = await self._db.execute(query, params)
        rows = await cursor.fetchall()
        return [dict(row) for row in rows]

    async def update_ha_entity(self, ha_id: int, **kwargs) -> None:
        allowed = {"enabled", "ha_component", "device_class", "unit", "icon", "entity_name"}
        fields = {k: v for k, v in kwargs.items() if k in allowed}
        if not fields:
            return
        set_clause = ", ".join(f"{k} = ?" for k in fields)
        values = list(fields.values()) + [ha_id]
        await self._db.execute(f"UPDATE ha_entities SET {set_clause} WHERE id = ?", values)
        await self._db.commit()

    # --- MQTT Mappings ---

    async def upsert_mqtt_mapping(
        self, datapoint_id: int, enabled: bool = True,
        custom_topic: Optional[str] = None, publish_json: bool = True
    ) -> None:
        await self._db.execute(
            """INSERT INTO mqtt_mappings (datapoint_id, enabled, custom_topic, publish_json)
               VALUES (?, ?, ?, ?)
               ON CONFLICT(datapoint_id) DO UPDATE SET
                 enabled = excluded.enabled,
                 custom_topic = excluded.custom_topic,
                 publish_json = excluded.publish_json""",
            (datapoint_id, int(enabled), custom_topic, int(publish_json)),
        )
        await self._db.commit()

    async def get_mqtt_mappings(self, enabled: Optional[bool] = None) -> list:
        query = """SELECT mm.*, dp.ecu_address, dp.did, dp.name as dp_name
                   FROM mqtt_mappings mm
                   JOIN datapoints dp ON mm.datapoint_id = dp.id
                   WHERE 1=1"""
        params = []
        if enabled is not None:
            query += " AND mm.enabled = ?"
            params.append(int(enabled))
        query += " ORDER BY dp.ecu_address, dp.did"
        cursor = await self._db.execute(query, params)
        rows = await cursor.fetchall()
        return [dict(row) for row in rows]

    # --- Schema Version ---

    async def get_schema_version(self) -> int:
        cursor = await self._db.execute("PRAGMA user_version")
        row = await cursor.fetchone()
        return row[0]

    # --- Backups ---

    async def create_backup(self) -> str:
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        filename = f"open3e_backup_{timestamp}.db"
        dest = self.backup_dir / filename
        await self._db.execute(f"VACUUM INTO '{dest}'")
        return filename

    async def list_backups(self) -> list:
        if not self.backup_dir.exists():
            return []
        backups = []
        for f in sorted(self.backup_dir.iterdir()):
            if f.suffix == ".db" and f.is_file():
                stat = f.stat()
                backups.append({
                    "filename": f.name,
                    "size_bytes": stat.st_size,
                    "created_at": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                })
        return backups

    async def get_backup_path(self, filename: str) -> Path:
        _validate_backup_filename(filename)
        path = self.backup_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"Backup not found: {filename}")
        # Extra safety: ensure resolved path is within backup_dir
        if not path.resolve().parent == self.backup_dir.resolve():
            raise ValueError(f"Invalid backup path: {filename}")
        return path

    async def delete_backup(self, filename: str) -> None:
        path = await self.get_backup_path(filename)
        path.unlink()
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/web/test_config_store.py -v
```

Expected: All tests pass.

- [ ] **Step 5: Commit**

```bash
git add src/open3e/web/config_store.py tests/web/test_config_store.py
git commit -m "Add ConfigStore — SQLite persistence for settings, ECUs, datapoints, HA, MQTT, backups"
```

---

### Task 3: CAN Interface Discovery

**Files:**
- Create: `src/open3e/web/can_discovery.py`
- Create: `tests/web/test_can_discovery.py`

- [ ] **Step 1: Write failing tests**

`tests/web/test_can_discovery.py`:
```python
import platform
from unittest.mock import patch, MagicMock
from open3e.web.can_discovery import discover_can_interfaces, get_can_status


class TestDiscoverCanInterfaces:
    def test_returns_list(self):
        """Should always return a list, even on non-Linux."""
        result = discover_can_interfaces()
        assert isinstance(result, list)

    @patch("open3e.web.can_discovery._is_linux", return_value=False)
    def test_empty_on_non_linux(self, mock_linux):
        result = discover_can_interfaces()
        assert result == []

    @patch("open3e.web.can_discovery._is_linux", return_value=True)
    @patch("open3e.web.can_discovery._read_sys_net")
    def test_finds_can_interfaces(self, mock_read, mock_linux):
        # CAN device type is 280 in /sys/class/net/<iface>/type
        mock_read.return_value = {
            "can0": {"type": "280", "operstate": "up"},
            "can1": {"type": "280", "operstate": "down"},
            "eth0": {"type": "1", "operstate": "up"},
            "vcan0": {"type": "280", "operstate": "unknown"},
        }
        result = discover_can_interfaces()
        names = [iface["name"] for iface in result]
        assert "can0" in names
        assert "can1" in names
        assert "vcan0" in names
        assert "eth0" not in names

    @patch("open3e.web.can_discovery._is_linux", return_value=True)
    @patch("open3e.web.can_discovery._read_sys_net")
    def test_includes_state(self, mock_read, mock_linux):
        mock_read.return_value = {
            "can0": {"type": "280", "operstate": "up"},
        }
        result = discover_can_interfaces()
        assert result[0]["name"] == "can0"
        assert result[0]["state"] == "up"


class TestGetCanStatus:
    @patch("open3e.web.can_discovery._is_linux", return_value=False)
    def test_unavailable_on_non_linux(self, mock_linux):
        result = get_can_status("can0")
        assert result["available"] is False

    @patch("open3e.web.can_discovery._is_linux", return_value=True)
    @patch("open3e.web.can_discovery._read_interface_stats")
    def test_reads_stats(self, mock_stats, mock_linux):
        mock_stats.return_value = {
            "state": "up",
            "rx_packets": 12345,
            "tx_packets": 678,
            "rx_errors": 0,
            "tx_errors": 0,
        }
        result = get_can_status("can0")
        assert result["available"] is True
        assert result["state"] == "up"
        assert result["rx_packets"] == 12345
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/web/test_can_discovery.py -v
```

Expected: `ModuleNotFoundError`

- [ ] **Step 3: Implement CAN discovery**

`src/open3e/web/can_discovery.py`:
```python
"""Detect available CAN interfaces on the host OS."""

import platform
from pathlib import Path
from typing import Optional

# CAN device type in /sys/class/net/<iface>/type
_CAN_ARPHRD = "280"


def _is_linux() -> bool:
    return platform.system() == "Linux"


def _read_sys_net() -> dict:
    """Read interface info from /sys/class/net/."""
    result = {}
    net_dir = Path("/sys/class/net")
    if not net_dir.exists():
        return result
    for iface_dir in net_dir.iterdir():
        if not iface_dir.is_dir():
            continue
        name = iface_dir.name
        type_file = iface_dir / "type"
        state_file = iface_dir / "operstate"
        iface_type = type_file.read_text().strip() if type_file.exists() else ""
        state = state_file.read_text().strip() if state_file.exists() else "unknown"
        result[name] = {"type": iface_type, "operstate": state}
    return result


def _read_interface_stats(name: str) -> Optional[dict]:
    """Read interface statistics from /sys/class/net/<name>/statistics/."""
    base = Path(f"/sys/class/net/{name}")
    if not base.exists():
        return None
    stats_dir = base / "statistics"
    state_file = base / "operstate"
    state = state_file.read_text().strip() if state_file.exists() else "unknown"

    def read_stat(stat_name: str) -> int:
        f = stats_dir / stat_name
        return int(f.read_text().strip()) if f.exists() else 0

    return {
        "state": state,
        "rx_packets": read_stat("rx_packets"),
        "tx_packets": read_stat("tx_packets"),
        "rx_errors": read_stat("rx_errors"),
        "tx_errors": read_stat("tx_errors"),
    }


def discover_can_interfaces() -> list:
    """Return a list of available CAN interfaces.

    Each entry is a dict: {"name": "can0", "state": "up"|"down"|"unknown"}

    Returns empty list on non-Linux platforms.
    """
    if not _is_linux():
        return []

    interfaces = []
    for name, info in _read_sys_net().items():
        if info["type"] == _CAN_ARPHRD:
            interfaces.append({
                "name": name,
                "state": info["operstate"],
            })
    return sorted(interfaces, key=lambda x: x["name"])


def get_can_status(interface: str) -> dict:
    """Get detailed status of a specific CAN interface.

    Returns dict with keys: available, state, rx_packets, tx_packets, rx_errors, tx_errors
    """
    if not _is_linux():
        return {"available": False, "interface": interface}

    stats = _read_interface_stats(interface)
    if stats is None:
        return {"available": False, "interface": interface}

    return {
        "available": True,
        "interface": interface,
        **stats,
    }
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/web/test_can_discovery.py -v
```

Expected: All tests pass.

- [ ] **Step 5: Commit**

```bash
git add src/open3e/web/can_discovery.py tests/web/test_can_discovery.py
git commit -m "Add CAN interface discovery module with /sys/class/net scanning"
```

---

### Task 4: Base template and layout

**Files:**
- Create: `src/open3e/web/templates/base.html`
- Create: `src/open3e/web/templates/dashboard.html`
- Create: `src/open3e/web/templates/login.html`

- [ ] **Step 1: Create the base layout template**

`src/open3e/web/templates/base.html`:
```html
<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %}open3e{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
          rel="stylesheet"
          integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YcnS/1p7u7sIZgXrdDeOccMmgBN6/2g6pOhB"
          crossorigin="anonymous">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"
          rel="stylesheet">
    <link href="/static/css/app.css" rel="stylesheet">
    {% block head %}{% endblock %}
</head>
<body>
    <!-- Sidebar -->
    <nav class="sidebar d-flex flex-column">
        <div class="mb-4">
            <h5 class="text-white mb-0">
                <i class="bi bi-thermometer-half me-2"></i>open3e
            </h5>
            <small class="text-muted">Web Interface</small>
        </div>

        <ul class="nav flex-column flex-grow-1">
            <li class="nav-item">
                <a class="nav-link {% if active_page == 'dashboard' %}active{% endif %}"
                   href="/">
                    <i class="bi bi-speedometer2 me-2"></i>Dashboard
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link {% if active_page == 'datapoints' %}active{% endif %}"
                   href="/datapoints">
                    <i class="bi bi-list-ul me-2"></i>Datapoints
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link {% if active_page == 'write' %}active{% endif %}"
                   href="/write">
                    <i class="bi bi-pencil-square me-2"></i>Write Values
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link {% if active_page == 'depict' %}active{% endif %}"
                   href="/depict">
                    <i class="bi bi-search me-2"></i>System Depiction
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link {% if active_page == 'settings' %}active{% endif %}"
                   href="/settings">
                    <i class="bi bi-gear me-2"></i>Settings
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link {% if active_page == 'system' %}active{% endif %}"
                   href="/system">
                    <i class="bi bi-info-circle me-2"></i>System Status
                </a>
            </li>
        </ul>

        <!-- Status bar -->
        <div class="status-bar">
            <div class="mb-1">
                <span class="status-dot" id="status-can"></span>
                <span>CAN: <span id="status-can-text">--</span></span>
            </div>
            <div class="mb-1">
                <span class="status-dot" id="status-mqtt"></span>
                <span>MQTT: <span id="status-mqtt-text">--</span></span>
            </div>
            <div>
                <span class="status-dot" id="status-engine"></span>
                <span>Engine: <span id="status-engine-text">--</span></span>
            </div>
        </div>
    </nav>

    <!-- Main content -->
    <main class="main-content">
        {% block content %}{% endblock %}
    </main>

    <!-- Toast container -->
    <div id="toast-container" class="toast-container"></div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
            crossorigin="anonymous"></script>
    <script src="/static/js/app.js"></script>
    {% block scripts %}{% endblock %}
</body>
</html>
```

- [ ] **Step 2: Create placeholder dashboard template**

`src/open3e/web/templates/dashboard.html`:
```html
{% extends "base.html" %}
{% block title %}Dashboard — open3e{% endblock %}

{% block content %}
<div class="d-flex justify-content-between align-items-center mb-4">
    <h2>Dashboard</h2>
</div>

{% if not ecus %}
<div class="alert alert-warning">
    <i class="bi bi-exclamation-triangle me-2"></i>
    No ECUs discovered yet.
    <a href="/depict">Run System Depiction</a> to scan for devices, or
    <a href="/settings">configure CAN interface</a> first.
</div>
{% else %}
<div class="row" id="dashboard-cards">
    <div class="col-12">
        <p class="text-muted">
            Dashboard with live data cards and charts will be available in a future update.
            <br>Go to <a href="/datapoints">Datapoints</a> to browse discovered data.
        </p>
    </div>
</div>
{% endif %}
{% endblock %}
```

- [ ] **Step 3: Create login template**

`src/open3e/web/templates/login.html`:
```html
<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Login — open3e</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
          rel="stylesheet"
          integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YcnS/1p7u7sIZgXrdDeOccMmgBN6/2g6pOhB"
          crossorigin="anonymous">
    <style>
        body { display: flex; align-items: center; justify-content: center; min-height: 100vh; }
        .login-card { max-width: 360px; width: 100%; }
    </style>
</head>
<body>
    <div class="login-card">
        <div class="card">
            <div class="card-body p-4">
                <h4 class="card-title text-center mb-3">
                    <i class="bi bi-thermometer-half me-2"></i>open3e
                </h4>
                {% if error %}
                <div class="alert alert-danger py-2">{{ error }}</div>
                {% endif %}
                <form method="POST" action="/login">
                    <div class="mb-3">
                        <input type="password" class="form-control" name="password"
                               placeholder="Password" autofocus required>
                    </div>
                    <button type="submit" class="btn btn-primary w-100">Login</button>
                </form>
            </div>
        </div>
    </div>
</body>
</html>
```

- [ ] **Step 4: Commit**

```bash
git add src/open3e/web/templates/
git commit -m "Add base layout, dashboard placeholder, and login templates"
```

---

### Task 5: Settings template

**Files:**
- Create: `src/open3e/web/templates/settings.html`

- [ ] **Step 1: Create the settings page with all four tabs**

`src/open3e/web/templates/settings.html`:
```html
{% extends "base.html" %}
{% block title %}Settings — open3e{% endblock %}

{% block content %}
<h2 class="mb-4">Settings</h2>

<ul class="nav nav-tabs" role="tablist">
    <li class="nav-item">
        <button class="nav-link active" data-bs-toggle="tab" data-bs-target="#tab-can">
            <i class="bi bi-plug me-1"></i>CAN
        </button>
    </li>
    <li class="nav-item">
        <button class="nav-link" data-bs-toggle="tab" data-bs-target="#tab-mqtt">
            <i class="bi bi-broadcast me-1"></i>MQTT
        </button>
    </li>
    <li class="nav-item">
        <button class="nav-link" data-bs-toggle="tab" data-bs-target="#tab-ha">
            <i class="bi bi-house me-1"></i>Home Assistant
        </button>
    </li>
    <li class="nav-item">
        <button class="nav-link" data-bs-toggle="tab" data-bs-target="#tab-system">
            <i class="bi bi-wrench me-1"></i>System
        </button>
    </li>
</ul>

<div class="tab-content settings-content">

    <!-- CAN Tab -->
    <div class="tab-pane fade show active" id="tab-can">
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">CAN Interface</h5>

                <div class="mb-3">
                    <label class="form-label">Detected Interfaces</label>
                    <div id="can-interfaces">
                        {% if can_interfaces %}
                            {% for iface in can_interfaces %}
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="can_interface"
                                       value="{{ iface.name }}" id="can-{{ iface.name }}"
                                       {% if settings.can_interface == iface.name %}checked{% endif %}>
                                <label class="form-check-label" for="can-{{ iface.name }}">
                                    {{ iface.name }}
                                    <span class="badge {% if iface.state == 'up' %}bg-success{% else %}bg-secondary{% endif %}">
                                        {{ iface.state }}
                                    </span>
                                </label>
                            </div>
                            {% endfor %}
                        {% else %}
                            <p class="text-muted">No CAN interfaces detected.</p>
                        {% endif %}
                    </div>
                    <button class="btn btn-sm btn-outline-secondary mt-2" onclick="refreshCanInterfaces()">
                        <i class="bi bi-arrow-clockwise me-1"></i>Refresh
                    </button>
                </div>

                <div class="mb-3">
                    <label class="form-label" for="can-manual">Manual Interface Name</label>
                    <input type="text" class="form-control" id="can-manual"
                           placeholder="e.g. can0" style="max-width: 200px;"
                           value="{{ settings.can_interface or '' }}">
                </div>

                <div class="mb-3">
                    <label class="form-label" for="can-bitrate">Bitrate</label>
                    <input type="number" class="form-control" id="can-bitrate"
                           value="{{ settings.can_bitrate or '250000' }}" style="max-width: 200px;">
                </div>

                <!-- Advanced CAN settings -->
                <div class="mb-3">
                    <a class="btn btn-sm btn-outline-secondary" data-bs-toggle="collapse"
                       href="#can-advanced">
                        <i class="bi bi-sliders me-1"></i>Advanced
                    </a>
                    <div class="collapse mt-3" id="can-advanced">
                        <div class="row g-3">
                            <div class="col-md-4">
                                <label class="form-label">Restart-ms</label>
                                <input type="number" class="form-control" id="can-restart-ms"
                                       value="{{ advanced_can.restart_ms | default('0') }}">
                            </div>
                            <div class="col-md-4">
                                <label class="form-label">TX Queue Length</label>
                                <input type="number" class="form-control" id="can-txqueuelen"
                                       value="{{ advanced_can.txqueuelen | default('10') }}">
                            </div>
                            <div class="col-md-4">
                                <label class="form-label">Sample Point</label>
                                <input type="text" class="form-control" id="can-sample-point"
                                       value="{{ advanced_can.sample_point | default('0.875') }}">
                            </div>
                            <div class="col-md-4">
                                <label class="form-label">SJW</label>
                                <input type="number" class="form-control" id="can-sjw"
                                       value="{{ advanced_can.sjw | default('1') }}">
                            </div>
                            <div class="col-md-4">
                                <div class="form-check mt-4">
                                    <input class="form-check-input" type="checkbox" id="can-listen-only"
                                           {% if advanced_can.listen_only %}checked{% endif %}>
                                    <label class="form-check-label" for="can-listen-only">Listen-only mode</label>
                                </div>
                            </div>
                            <div class="col-md-4">
                                <div class="form-check mt-4">
                                    <input class="form-check-input" type="checkbox" id="can-loopback"
                                           {% if advanced_can.loopback %}checked{% endif %}>
                                    <label class="form-check-label" for="can-loopback">Loopback</label>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <button class="btn btn-primary" onclick="saveCanSettings()">
                    <i class="bi bi-check-lg me-1"></i>Apply &amp; Connect
                </button>
            </div>
        </div>
    </div>

    <!-- MQTT Tab -->
    <div class="tab-pane fade" id="tab-mqtt">
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">MQTT Broker</h5>
                <div class="row g-3">
                    <div class="col-md-8">
                        <label class="form-label">Host</label>
                        <input type="text" class="form-control" id="mqtt-host"
                               value="{{ settings.mqtt_host or '' }}" placeholder="192.168.1.1">
                    </div>
                    <div class="col-md-4">
                        <label class="form-label">Port</label>
                        <input type="number" class="form-control" id="mqtt-port"
                               value="{{ settings.mqtt_port or '1883' }}">
                    </div>
                    <div class="col-md-6">
                        <label class="form-label">Username</label>
                        <input type="text" class="form-control" id="mqtt-user"
                               value="{{ settings.mqtt_user or '' }}">
                    </div>
                    <div class="col-md-6">
                        <label class="form-label">Password</label>
                        <input type="password" class="form-control" id="mqtt-password"
                               value="{{ settings.mqtt_password or '' }}">
                    </div>
                </div>

                <hr>
                <h6>TLS</h6>
                <div class="form-check mb-3">
                    <input class="form-check-input" type="checkbox" id="mqtt-tls"
                           {% if settings.mqtt_tls_enabled == '1' %}checked{% endif %}
                           onchange="document.getElementById('mqtt-tls-options').classList.toggle('d-none', !this.checked)">
                    <label class="form-check-label" for="mqtt-tls">Enable TLS</label>
                </div>
                <div id="mqtt-tls-options" class="{% if settings.mqtt_tls_enabled != '1' %}d-none{% endif %}">
                    <div class="mb-3">
                        <label class="form-label">CA Certificate (PEM)</label>
                        <input type="file" class="form-control" id="mqtt-ca-cert" accept=".pem,.crt,.cer">
                        {% if settings.mqtt_ca_cert %}
                        <small class="text-success"><i class="bi bi-check-circle me-1"></i>Certificate uploaded</small>
                        {% endif %}
                    </div>
                </div>

                <hr>
                <h6>Topic Configuration</h6>
                <div class="row g-3">
                    <div class="col-md-4">
                        <label class="form-label">Topic Prefix</label>
                        <input type="text" class="form-control" id="mqtt-prefix"
                               value="{{ settings.mqtt_topic_prefix or 'open3e' }}">
                    </div>
                    <div class="col-md-4">
                        <label class="form-label">Format String</label>
                        <input type="text" class="form-control" id="mqtt-format"
                               value="{{ settings.mqtt_format_string or '{didName}' }}"
                               oninput="updateMqttPreview()">
                    </div>
                    <div class="col-md-4">
                        <label class="form-label">Client ID</label>
                        <input type="text" class="form-control" id="mqtt-client-id"
                               value="{{ settings.mqtt_client_id or '' }}" placeholder="auto-generated">
                    </div>
                    <div class="col-12">
                        <small class="text-muted">Preview: <code id="mqtt-preview">open3e/FlowTemperatureSensor</code></small>
                    </div>
                </div>

                <div class="mt-3">
                    <button class="btn btn-outline-secondary me-2" onclick="testMqtt()">
                        <i class="bi bi-wifi me-1"></i>Test Connection
                    </button>
                    <button class="btn btn-primary" onclick="saveMqttSettings()">
                        <i class="bi bi-check-lg me-1"></i>Save &amp; Reconnect
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- Home Assistant Tab -->
    <div class="tab-pane fade" id="tab-ha">
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">Home Assistant Discovery</h5>

                <div class="form-check form-switch mb-3">
                    <input class="form-check-input" type="checkbox" id="ha-enabled"
                           {% if settings.ha_discovery_enabled == '1' %}checked{% endif %}>
                    <label class="form-check-label" for="ha-enabled">Enable MQTT Auto-Discovery</label>
                </div>

                <div class="mb-3">
                    <label class="form-label">Discovery Prefix</label>
                    <input type="text" class="form-control" id="ha-prefix"
                           value="{{ settings.ha_discovery_prefix or 'homeassistant' }}"
                           style="max-width: 300px;">
                </div>

                <div class="mb-3">
                    <button class="btn btn-outline-secondary" onclick="applyHaDefaults()">
                        <i class="bi bi-magic me-1"></i>Apply Suggested Defaults
                    </button>
                </div>

                <div class="table-responsive">
                    <table class="table table-sm table-hover" id="ha-entities-table">
                        <thead>
                            <tr>
                                <th>Enabled</th>
                                <th>ECU</th>
                                <th>DID</th>
                                <th>Name</th>
                                <th>Sub-field</th>
                                <th>Component</th>
                                <th>Device Class</th>
                                <th>Unit</th>
                                <th>Icon</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for entity in ha_entities %}
                            <tr>
                                <td>
                                    <div class="form-check form-switch">
                                        <input class="form-check-input" type="checkbox"
                                               {% if entity.enabled %}checked{% endif %}
                                               onchange="toggleHaEntity({{ entity.id }}, this.checked)">
                                    </div>
                                </td>
                                <td>{{ "0x%03x" | format(entity.ecu_address) }}</td>
                                <td>{{ entity.did }}</td>
                                <td>{{ entity.dp_name }}</td>
                                <td>{{ entity.sub_field or '—' }}</td>
                                <td>{{ entity.ha_component }}</td>
                                <td>{{ entity.device_class or '—' }}</td>
                                <td>{{ entity.unit or '—' }}</td>
                                <td>{{ entity.icon or '—' }}</td>
                                <td>
                                    <button class="btn btn-sm btn-outline-secondary"
                                            onclick="editHaEntity({{ entity.id }})">
                                        <i class="bi bi-pencil"></i>
                                    </button>
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>

                <button class="btn btn-primary" onclick="saveHaSettings()">
                    <i class="bi bi-check-lg me-1"></i>Save
                </button>
            </div>
        </div>
    </div>

    <!-- System Tab -->
    <div class="tab-pane fade" id="tab-system">
        <div class="row g-4">
            <!-- Database Backup -->
            <div class="col-12">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Database</h5>
                        <button class="btn btn-outline-primary mb-3" onclick="createBackup()">
                            <i class="bi bi-download me-1"></i>Create Backup
                        </button>

                        <div class="mb-3">
                            <label class="form-label">Restore from file</label>
                            <input type="file" class="form-control" id="backup-upload"
                                   accept=".db" style="max-width: 400px;">
                            <button class="btn btn-sm btn-outline-warning mt-2" onclick="restoreBackup()">
                                <i class="bi bi-upload me-1"></i>Restore
                            </button>
                        </div>

                        <table class="table table-sm" id="backup-table">
                            <thead>
                                <tr>
                                    <th>Filename</th>
                                    <th>Created</th>
                                    <th>Size</th>
                                    <th></th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for backup in backups %}
                                <tr>
                                    <td>{{ backup.filename }}</td>
                                    <td>{{ backup.created_at }}</td>
                                    <td>{{ "%.1f KB" | format(backup.size_bytes / 1024) }}</td>
                                    <td>
                                        <a href="/api/backup/{{ backup.filename }}" class="btn btn-sm btn-outline-primary">
                                            <i class="bi bi-download"></i>
                                        </a>
                                        <button class="btn btn-sm btn-outline-danger"
                                                onclick="deleteBackup('{{ backup.filename }}')">
                                            <i class="bi bi-trash"></i>
                                        </button>
                                    </td>
                                </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- Authentication -->
            <div class="col-md-6">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Authentication</h5>
                        <div class="form-check form-switch mb-3">
                            <input class="form-check-input" type="checkbox" id="auth-enabled"
                                   {% if settings.auth_enabled == '1' %}checked{% endif %}>
                            <label class="form-check-label" for="auth-enabled">Enable Password Protection</label>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Password</label>
                            <input type="password" class="form-control" id="auth-password"
                                   placeholder="Set new password" style="max-width: 300px;">
                        </div>
                        <button class="btn btn-primary" onclick="saveAuthSettings()">
                            <i class="bi bi-check-lg me-1"></i>Save
                        </button>
                    </div>
                </div>
            </div>

            <!-- Web Server -->
            <div class="col-md-6">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Web Server</h5>
                        <div class="mb-3">
                            <label class="form-label">Port (requires restart)</label>
                            <input type="number" class="form-control" id="web-port"
                                   value="{{ settings.web_port or '8080' }}" style="max-width: 150px;">
                        </div>
                        <button class="btn btn-primary" onclick="saveWebSettings()">
                            <i class="bi bi-check-lg me-1"></i>Save
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>

</div><!-- tab-content -->
{% endblock %}

{% block scripts %}
<script>
function getSelectedCanInterface() {
    const radio = document.querySelector('input[name="can_interface"]:checked');
    const manual = document.getElementById("can-manual").value.trim();
    return manual || (radio ? radio.value : "");
}

async function refreshCanInterfaces() {
    const data = await apiCall("/api/can/interfaces", "GET");
    // Reload page to show updated list
    location.reload();
}

async function saveCanSettings() {
    const iface = getSelectedCanInterface();
    if (!iface) { showToast("Please select or enter a CAN interface", "warning"); return; }
    const advanced = {};
    const restartMs = document.getElementById("can-restart-ms");
    if (restartMs) advanced.restart_ms = restartMs.value;
    const txql = document.getElementById("can-txqueuelen");
    if (txql) advanced.txqueuelen = txql.value;
    const sp = document.getElementById("can-sample-point");
    if (sp) advanced.sample_point = sp.value;
    const sjw = document.getElementById("can-sjw");
    if (sjw) advanced.sjw = sjw.value;
    const lo = document.getElementById("can-listen-only");
    if (lo) advanced.listen_only = lo.checked;
    const lb = document.getElementById("can-loopback");
    if (lb) advanced.loopback = lb.checked;

    await apiCall("/api/settings", "PATCH", {
        can_interface: iface,
        can_bitrate: document.getElementById("can-bitrate").value,
        can_advanced_params: JSON.stringify(advanced),
    });
    showToast("CAN settings saved", "success");
}

function updateMqttPreview() {
    const prefix = document.getElementById("mqtt-prefix").value || "open3e";
    const fmt = document.getElementById("mqtt-format").value || "{didName}";
    // Simple preview with example values
    const preview = prefix + "/" + fmt
        .replace("{didName}", "FlowTemperatureSensor")
        .replace("{didNumber}", "268")
        .replace("{ecuAddr}", "680")
        .replace("{device}", "vitocal");
    document.getElementById("mqtt-preview").textContent = preview;
}

async function testMqtt() {
    const result = await apiCall("/api/settings/test-mqtt", "POST", {
        mqtt_host: document.getElementById("mqtt-host").value,
        mqtt_port: parseInt(document.getElementById("mqtt-port").value),
        mqtt_user: document.getElementById("mqtt-user").value,
        mqtt_password: document.getElementById("mqtt-password").value,
        mqtt_tls_enabled: document.getElementById("mqtt-tls").checked,
    });
    if (result.success) {
        showToast("MQTT connection successful", "success");
    } else {
        showToast("MQTT connection failed: " + result.error, "danger");
    }
}

async function saveMqttSettings() {
    const settings = {
        mqtt_host: document.getElementById("mqtt-host").value,
        mqtt_port: document.getElementById("mqtt-port").value,
        mqtt_user: document.getElementById("mqtt-user").value,
        mqtt_password: document.getElementById("mqtt-password").value,
        mqtt_tls_enabled: document.getElementById("mqtt-tls").checked ? "1" : "0",
        mqtt_topic_prefix: document.getElementById("mqtt-prefix").value,
        mqtt_format_string: document.getElementById("mqtt-format").value,
        mqtt_client_id: document.getElementById("mqtt-client-id").value,
    };
    // Handle CA cert file upload
    const certInput = document.getElementById("mqtt-ca-cert");
    if (certInput.files.length > 0) {
        const reader = new FileReader();
        reader.onload = async function(e) {
            settings.mqtt_ca_cert = btoa(e.target.result);
            await apiCall("/api/settings", "PATCH", settings);
            showToast("MQTT settings saved", "success");
        };
        reader.readAsText(certInput.files[0]);
    } else {
        await apiCall("/api/settings", "PATCH", settings);
        showToast("MQTT settings saved", "success");
    }
}

async function applyHaDefaults() {
    await apiCall("/api/ha/apply-defaults", "POST");
    showToast("Smart defaults applied — review and enable entities", "success");
    location.reload();
}

async function toggleHaEntity(id, enabled) {
    await apiCall("/api/ha/entities/" + id, "PATCH", { enabled: enabled });
}

function editHaEntity(id) {
    // Placeholder — will open modal in Plan 3
    showToast("Entity edit modal coming soon", "info");
}

async function saveHaSettings() {
    await apiCall("/api/settings", "PATCH", {
        ha_discovery_enabled: document.getElementById("ha-enabled").checked ? "1" : "0",
        ha_discovery_prefix: document.getElementById("ha-prefix").value,
    });
    showToast("HA settings saved", "success");
}

async function createBackup() {
    await apiCall("/api/backup", "POST");
    showToast("Backup created", "success");
    location.reload();
}

async function deleteBackup(filename) {
    if (!confirm("Delete backup " + filename + "?")) return;
    await apiCall("/api/backup/" + filename, "DELETE");
    showToast("Backup deleted", "success");
    location.reload();
}

async function restoreBackup() {
    const input = document.getElementById("backup-upload");
    if (!input.files.length) { showToast("Select a file first", "warning"); return; }
    if (!confirm("This will replace all settings. Continue?")) return;
    const formData = new FormData();
    formData.append("file", input.files[0]);
    const resp = await fetch("/api/backup/restore", { method: "POST", body: formData });
    if (resp.ok) {
        showToast("Backup restored. Reloading...", "success");
        setTimeout(() => location.reload(), 2000);
    } else {
        const err = await resp.json();
        showToast("Restore failed: " + (err.detail || "unknown error"), "danger");
    }
}

async function saveAuthSettings() {
    const settings = {
        auth_enabled: document.getElementById("auth-enabled").checked ? "1" : "0",
    };
    const pw = document.getElementById("auth-password").value;
    if (pw) settings.auth_password = pw;
    await apiCall("/api/auth/settings", "PATCH", settings);
    showToast("Authentication settings saved", "success");
}

async function saveWebSettings() {
    await apiCall("/api/settings", "PATCH", {
        web_port: document.getElementById("web-port").value,
    });
    showToast("Web server port saved. Restart required.", "warning");
}

// Init preview on load
updateMqttPreview();
</script>
{% endblock %}
```

- [ ] **Step 2: Commit**

```bash
git add src/open3e/web/templates/settings.html
git commit -m "Add settings page with CAN, MQTT, HA, and system configuration tabs"
```

---

### Task 6: FastAPI server with routes

**Files:**
- Create: `src/open3e/web/server.py`
- Create: `src/open3e/web/auth.py`
- Create: `tests/web/test_server.py`

- [ ] **Step 1: Write failing tests for the server routes**

`tests/web/test_server.py`:
```python
import os
import pytest
import asyncio
from httpx import AsyncClient, ASGITransport

from open3e.web.server import create_app
from open3e.web.config_store import ConfigStore

TEST_DB = "/tmp/open3e_test_server.db"


@pytest.fixture
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def store():
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    s = ConfigStore(TEST_DB)
    asyncio.get_event_loop().run_until_complete(s.initialize())
    yield s
    asyncio.get_event_loop().run_until_complete(s.close())
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)


@pytest.fixture
def app(store):
    return create_app(store)


def run(coro):
    return asyncio.get_event_loop().run_until_complete(coro)


class TestPages:
    def test_dashboard_loads(self, app, store):
        async def _test():
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as client:
                resp = await client.get("/")
                assert resp.status_code == 200
                assert "open3e" in resp.text
        run(_test())

    def test_settings_loads(self, app, store):
        async def _test():
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as client:
                resp = await client.get("/settings")
                assert resp.status_code == 200
                assert "CAN" in resp.text
        run(_test())


class TestSettingsApi:
    def test_get_settings(self, app, store):
        async def _test():
            await store.set_setting("mqtt_host", "10.0.0.1")
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as client:
                resp = await client.get("/api/settings")
                assert resp.status_code == 200
                data = resp.json()
                assert data["mqtt_host"] == "10.0.0.1"
        run(_test())

    def test_patch_settings(self, app, store):
        async def _test():
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as client:
                resp = await client.patch("/api/settings", json={"mqtt_host": "192.168.1.1", "mqtt_port": "8883"})
                assert resp.status_code == 200
                val = await store.get_setting("mqtt_host")
                assert val == "192.168.1.1"
        run(_test())


class TestCanInterfacesApi:
    def test_list_interfaces(self, app, store):
        async def _test():
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as client:
                resp = await client.get("/api/can/interfaces")
                assert resp.status_code == 200
                assert isinstance(resp.json(), list)
        run(_test())


class TestBackupApi:
    def test_create_and_list(self, app, store):
        async def _test():
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as client:
                resp = await client.post("/api/backup")
                assert resp.status_code == 200
                filename = resp.json()["filename"]

                resp = await client.get("/api/backups")
                assert resp.status_code == 200
                filenames = [b["filename"] for b in resp.json()]
                assert filename in filenames
        run(_test())

    def test_download(self, app, store):
        async def _test():
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as client:
                resp = await client.post("/api/backup")
                filename = resp.json()["filename"]

                resp = await client.get(f"/api/backup/{filename}")
                assert resp.status_code == 200
                assert len(resp.content) > 0
        run(_test())

    def test_delete(self, app, store):
        async def _test():
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as client:
                resp = await client.post("/api/backup")
                filename = resp.json()["filename"]

                resp = await client.delete(f"/api/backup/{filename}")
                assert resp.status_code == 200

                resp = await client.get("/api/backups")
                filenames = [b["filename"] for b in resp.json()]
                assert filename not in filenames
        run(_test())
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/web/test_server.py -v
```

Expected: `ModuleNotFoundError: No module named 'open3e.web.server'`

- [ ] **Step 3: Create auth stub**

`src/open3e/web/auth.py`:
```python
"""Optional password authentication middleware (stub — full impl in Plan 3)."""

import hashlib
import os
from typing import Optional


def hash_password(password: str) -> str:
    """Hash a password using scrypt. Returns hex-encoded salt:hash."""
    salt = os.urandom(16)
    dk = hashlib.scrypt(password.encode(), salt=salt, n=16384, r=8, p=1, dklen=32)
    return salt.hex() + ":" + dk.hex()


def verify_password(password: str, stored_hash: str) -> bool:
    """Verify a password against a stored scrypt hash."""
    parts = stored_hash.split(":")
    if len(parts) != 2:
        return False
    salt = bytes.fromhex(parts[0])
    expected = bytes.fromhex(parts[1])
    dk = hashlib.scrypt(password.encode(), salt=salt, n=16384, r=8, p=1, dklen=32)
    return dk == expected
```

- [ ] **Step 4: Implement the FastAPI server**

`src/open3e/web/server.py`:
```python
"""FastAPI web server for open3e — routes, templates, static files."""

import json
import os
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Request, HTTPException, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from open3e.web.config_store import ConfigStore
from open3e.web.can_discovery import discover_can_interfaces
from open3e.web.auth import hash_password

WEB_DIR = Path(__file__).parent
TEMPLATES_DIR = WEB_DIR / "templates"
STATIC_DIR = WEB_DIR / "static"


def create_app(store: ConfigStore) -> FastAPI:
    app = FastAPI(title="open3e Web UI")
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
    templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

    # Store reference for routes
    app.state.store = store

    # --- Page Routes ---

    @app.get("/", response_class=HTMLResponse)
    async def dashboard(request: Request):
        ecus = await store.get_ecus()
        return templates.TemplateResponse("dashboard.html", {
            "request": request,
            "active_page": "dashboard",
            "ecus": ecus,
        })

    @app.get("/settings", response_class=HTMLResponse)
    async def settings_page(request: Request):
        settings = await store.get_all_settings()
        can_interfaces = discover_can_interfaces()
        ha_entities = await store.get_ha_entities()
        backups = await store.list_backups()
        # Parse advanced CAN params
        advanced_can = {}
        if settings.get("can_advanced_params"):
            try:
                advanced_can = json.loads(settings["can_advanced_params"])
            except (json.JSONDecodeError, TypeError):
                pass
        return templates.TemplateResponse("settings.html", {
            "request": request,
            "active_page": "settings",
            "settings": settings,
            "can_interfaces": can_interfaces,
            "advanced_can": advanced_can,
            "ha_entities": ha_entities,
            "backups": backups,
        })

    # --- Settings API ---

    @app.get("/api/settings")
    async def get_settings():
        return await store.get_all_settings()

    @app.patch("/api/settings")
    async def patch_settings(request: Request):
        body = await request.json()
        for key, value in body.items():
            await store.set_setting(key, str(value))
        return {"status": "ok"}

    # --- CAN Interfaces API ---

    @app.get("/api/can/interfaces")
    async def list_can_interfaces():
        return discover_can_interfaces()

    # --- ECUs API ---

    @app.get("/api/ecus")
    async def list_ecus():
        return await store.get_ecus()

    # --- Datapoints API ---

    @app.get("/api/datapoints")
    async def list_datapoints(
        ecu: Optional[int] = None,
        priority: Optional[int] = None,
    ):
        return await store.get_datapoints(ecu_address=ecu, poll_priority=priority)

    @app.patch("/api/datapoints/{dp_id}")
    async def update_datapoint(dp_id: int, request: Request):
        body = await request.json()
        await store.update_datapoint(dp_id, **body)
        return {"status": "ok"}

    # --- HA Entities API ---

    @app.get("/api/ha/entities")
    async def list_ha_entities(enabled: Optional[bool] = None):
        return await store.get_ha_entities(enabled=enabled)

    @app.patch("/api/ha/entities/{ha_id}")
    async def update_ha_entity(ha_id: int, request: Request):
        body = await request.json()
        await store.update_ha_entity(ha_id, **body)
        return {"status": "ok"}

    @app.post("/api/ha/apply-defaults")
    async def apply_ha_defaults():
        # Stub — full implementation in Plan 3 with ha_discovery.py
        return {"status": "ok", "message": "Smart defaults will be available after system depiction"}

    # --- MQTT Mappings API ---

    @app.get("/api/mqtt/mappings")
    async def list_mqtt_mappings(enabled: Optional[bool] = None):
        return await store.get_mqtt_mappings(enabled=enabled)

    # --- MQTT Test ---

    @app.post("/api/settings/test-mqtt")
    async def test_mqtt_connection(request: Request):
        body = await request.json()
        try:
            import paho.mqtt.client as paho
            client = paho.Client(paho.CallbackAPIVersion.VERSION2, "open3e_test")
            if body.get("mqtt_user"):
                client.username_pw_set(body["mqtt_user"], body.get("mqtt_password", ""))
            client.connect(body["mqtt_host"], int(body.get("mqtt_port", 1883)), keepalive=5)
            client.disconnect()
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}

    # --- Backup API ---

    @app.post("/api/backup")
    async def create_backup():
        filename = await store.create_backup()
        return {"filename": filename}

    @app.get("/api/backups")
    async def list_backups():
        return await store.list_backups()

    @app.get("/api/backup/{filename}")
    async def download_backup(filename: str):
        try:
            path = await store.get_backup_path(filename)
            return FileResponse(path, filename=filename, media_type="application/octet-stream")
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail="Backup not found")

    @app.delete("/api/backup/{filename}")
    async def delete_backup(filename: str):
        try:
            await store.delete_backup(filename)
            return {"status": "ok"}
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail="Backup not found")

    @app.post("/api/backup/restore")
    async def restore_backup(file: UploadFile = File(...)):
        if not file.filename.endswith(".db"):
            raise HTTPException(status_code=400, detail="File must be a .db file")
        # Save uploaded file to temp location
        import tempfile, shutil
        with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name
        # Replace database — in production, this would stop the engine first
        try:
            import shutil as sh
            sh.copy2(tmp_path, store.db_path)
            os.unlink(tmp_path)
            # Re-initialize to reload schema
            await store.close()
            await store.initialize()
            return {"status": "ok"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    # --- Auth API ---

    @app.patch("/api/auth/settings")
    async def update_auth_settings(request: Request):
        body = await request.json()
        if "auth_enabled" in body:
            await store.set_setting("auth_enabled", body["auth_enabled"])
        if "auth_password" in body:
            hashed = hash_password(body["auth_password"])
            await store.set_setting("auth_password_hash", hashed)
        return {"status": "ok"}

    # --- Status API ---

    @app.get("/api/status")
    async def system_status():
        import sys
        try:
            from importlib.metadata import version
            open3e_version = version("open3e")
        except Exception:
            open3e_version = "unknown"
        return {
            "open3e_version": open3e_version,
            "python_version": sys.version,
        }

    return app
```

- [ ] **Step 5: Run tests to verify they pass**

```bash
pip install httpx  # test dependency
pytest tests/web/test_server.py -v
```

Expected: All tests pass.

- [ ] **Step 6: Commit**

```bash
git add src/open3e/web/server.py src/open3e/web/auth.py tests/web/test_server.py
git commit -m "Add FastAPI server with settings, backup, CAN, HA, and MQTT API routes"
```

---

### Task 7: Launcher — the entry point

**Files:**
- Create: `src/open3e/web/launcher.py`

- [ ] **Step 1: Implement the launcher**

`src/open3e/web/launcher.py`:
```python
"""Entry point for open3e web UI.

Usage: open3e-web
No arguments required. All configuration via web interface.
"""

import asyncio
import socket
import sys

import uvicorn

from open3e.web.config_store import ConfigStore
from open3e.web.server import create_app

# Default database path (in current working directory)
DEFAULT_DB_PATH = "open3e_web.db"
DEFAULT_PORT = 8080
MAX_PORT_ATTEMPTS = 10


def _get_local_ip() -> str:
    """Best-effort detection of the machine's LAN IP address."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def _port_available(port: int) -> bool:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("0.0.0.0", port))
        s.close()
        return True
    except OSError:
        return False


def _find_port(preferred: int) -> int:
    """Find an available port starting from preferred."""
    for offset in range(MAX_PORT_ATTEMPTS):
        port = preferred + offset
        if _port_available(port):
            return port
    return preferred  # Fall back, uvicorn will error if truly unavailable


def main():
    # Initialize database
    store = ConfigStore(DEFAULT_DB_PATH)
    loop = asyncio.new_event_loop()
    loop.run_until_complete(store.initialize())

    # Read configured port or use default
    port_str = loop.run_until_complete(store.get_setting("web_port"))
    preferred_port = int(port_str) if port_str else DEFAULT_PORT
    port = _find_port(preferred_port)

    # Create FastAPI app
    app = create_app(store)

    # Print startup info
    local_ip = _get_local_ip()
    print(f"open3e-web starting...")
    print(f"  Local:   http://127.0.0.1:{port}")
    print(f"  Network: http://{local_ip}:{port}")
    print()
    print("Configure CAN interface and run System Depiction via the web interface.")
    print("Press Ctrl+C to stop.")

    # Run uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="warning")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Verify the entry point works**

```bash
python -m open3e.web.launcher &
sleep 2
curl -s http://localhost:8080/ | head -5
kill %1
```

Expected: HTML output containing "open3e".

- [ ] **Step 3: Commit**

```bash
git add src/open3e/web/launcher.py
git commit -m "Add launcher entry point — single command starts web UI with auto port detection"
```

---

### Task 8: Integration test — full startup

**Files:**
- Modify: `tests/web/test_server.py` (add integration test)

- [ ] **Step 1: Add an end-to-end startup test**

Append to `tests/web/test_server.py`:

```python
class TestIntegration:
    def test_full_settings_roundtrip(self, app, store):
        """Save CAN + MQTT settings, reload settings page, verify values."""
        async def _test():
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as client:
                # Save settings via API
                resp = await client.patch("/api/settings", json={
                    "can_interface": "can0",
                    "can_bitrate": "250000",
                    "mqtt_host": "192.168.1.100",
                    "mqtt_port": "1883",
                    "mqtt_topic_prefix": "open3e",
                    "ha_discovery_enabled": "1",
                    "ha_discovery_prefix": "homeassistant",
                })
                assert resp.status_code == 200

                # Read back via API
                resp = await client.get("/api/settings")
                data = resp.json()
                assert data["can_interface"] == "can0"
                assert data["mqtt_host"] == "192.168.1.100"
                assert data["ha_discovery_enabled"] == "1"

                # Load settings page — should render without error
                resp = await client.get("/settings")
                assert resp.status_code == 200
                assert "192.168.1.100" in resp.text
                assert "can0" in resp.text
        run(_test())
```

- [ ] **Step 2: Run all tests**

```bash
pytest tests/web/ -v
```

Expected: All tests pass.

- [ ] **Step 3: Commit**

```bash
git add tests/web/test_server.py
git commit -m "Add integration test for settings roundtrip via API and page render"
```

---

## Summary

After completing Plan 1, you have:

- A working `open3e-web` command that launches a FastAPI server
- SQLite database with full schema for settings, ECUs, datapoints, HA entities, MQTT mappings
- CAN interface discovery (Linux-only, graceful degradation)
- Settings page with CAN, MQTT, HA, and System tabs — all functional
- Database backup/restore/download/delete via web UI
- Auth password hashing (stub middleware — activated in Plan 3)
- Bootstrap 5 dark theme with sidebar navigation
- REST API for all CRUD operations
- Test suite covering config store, CAN discovery, server routes, and integration

**Next:** Plan 2 adds the CAN engine, priority scheduler, WebSocket live data, dashboard with charts, datapoints browser, and write values page.
