# Web UI Plan 3: MQTT, HA Discovery & Auth

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add MQTT publishing with per-datapoint topic mapping, Home Assistant MQTT auto-discovery with smart defaults inference, HA command handling (write from HA), and optional password authentication middleware. This completes the feature set defined in the design spec.

**Architecture:** The MQTT publisher subscribes to CAN engine data events and publishes to the configured broker. HA discovery publishes config payloads to `homeassistant/<component>/<id>/config`. The auth middleware wraps FastAPI routes with session-cookie-based password protection when enabled.

**Tech Stack:** paho-mqtt (existing dependency), hashlib.scrypt (stdlib), FastAPI middleware

**Spec reference:** `docs/specs/2026-04-06-web-ui-design.md`
**Depends on:** Plan 1 (config_store, server, auth) + Plan 2 (can_engine, ws_manager)

---

## File Map

```
src/open3e/web/
  mqtt_publisher.py      NEW - MQTT client, publish loop, TLS, reconfiguration
  ha_discovery.py        NEW - smart defaults inference, discovery payloads, command handling
  auth.py                MODIFY - add session middleware, login/logout flow
  server.py              MODIFY - integrate MQTT publisher, mount auth middleware
  launcher.py            MODIFY - start MQTT publisher, wire to engine data
  templates/
    login.html           MODIFY - wire to actual auth flow

tests/web/
  test_mqtt_publisher.py NEW
  test_ha_discovery.py   NEW
  test_auth.py           NEW
```

---

### Task 1: HA Discovery — Smart Defaults Inference

**Files:**
- Create: `src/open3e/web/ha_discovery.py`
- Create: `tests/web/test_ha_discovery.py`

### ha_discovery.py

Module with:

`INFERENCE_RULES` — list of tuples: `(name_pattern, codec_types, ha_component, device_class, unit, icon)`:
- `("*Temperature*", ["O3EComplexType","O3EInt16"], "sensor", "temperature", "°C", "mdi:thermometer")`
- `("*Pressure*", ["O3EComplexType","O3EInt16"], "sensor", "pressure", "bar", "mdi:gauge")`
- `("*Energy*", ["O3EInt32","O3EInt64"], "sensor", "energy", "kWh", "mdi:lightning-bolt")`
- `("*FlowMeter*", ["O3EInt32"], "sensor", "water", "L", "mdi:water")`
- `("*Power*", ["O3EInt16","O3EInt32"], "sensor", "power", "W", "mdi:flash")`
- `("*OperationMode*", ["O3EEnum"], "select", None, None, "mdi:cog")`
- `("*OperationState*", ["O3EEnum"], "select", None, None, "mdi:toggle-switch")`
- `("*Setpoint*", ["O3EComplexType","O3EInt16"], "number", "temperature", "°C", "mdi:thermostat")`
- `("*Pump*", ["O3EBool"], "binary_sensor", None, None, "mdi:pump")`

`infer_ha_entity(dp_name, codec_type, is_writable)` -> dict or None:
- Match dp_name against patterns using fnmatch
- For ComplexType DIDs, set sub_field="Actual"
- For writable setpoints, use "number" component
- Return dict with: ha_component, device_class, unit, icon, sub_field, entity_name (human-readable from dp_name)
- Return None if no rule matches

`build_discovery_payload(entity, ecu, topic_prefix, ha_prefix)` -> tuple(topic, payload):
- topic: `{ha_prefix}/{component}/open3e_{ecu_hex}_{did}_{sub}/config`
- payload: dict with name, unique_id, state_topic, device_class, unit_of_measurement, icon, device (identifiers, name, manufacturer "Viessmann", via_device "open3e")
- For writable entities (number, select): add command_topic

`build_removal_payload(entity, ecu, ha_prefix)` -> tuple(topic, empty_bytes):
- Same topic as discovery, but payload is empty bytes (removes from HA)

### test_ha_discovery.py

Tests:
- test_infer_temperature: "FlowTemperatureSensor" + "O3EComplexType" -> sensor, temperature, °C, sub_field=Actual
- test_infer_pressure: "WaterPressureSensor" + "O3EComplexType" -> sensor, pressure, bar
- test_infer_setpoint_writable: "DomesticHotWaterTemperatureSetpoint" + "O3EInt16", is_writable=True -> number
- test_infer_enum: "ExternalDomesticHotWaterTargetOperationMode" + "O3EEnum" -> select
- test_infer_pump: "DomesticHotWaterCirculationPump" + "O3EBool" -> binary_sensor
- test_infer_unknown_returns_none: "SomeRandomName" + "RawCodec" -> None
- test_build_discovery_payload: verify topic format, required keys, device block
- test_build_removal_payload: verify topic same, payload empty

## Your Job

Write tests first, implement, run tests, commit: "Add HA discovery smart defaults inference and payload builder"

---

### Task 2: MQTT Publisher

**Files:**
- Create: `src/open3e/web/mqtt_publisher.py`
- Create: `tests/web/test_mqtt_publisher.py`

### mqtt_publisher.py

Class `MqttPublisher`:
- `__init__(store, on_status)` — stores refs, no connection yet
- `async configure()` — reads MQTT settings from store, returns False if host not set
- `start()` — creates paho.mqtt.client, sets callbacks, connects (with TLS if enabled: decode base64 CA cert from settings, write to tempfile, call tls_set). Starts mqtt loop_start().
- `stop()` — publishes LWT offline, disconnects, loop_stop
- `reconfigure()` — stop + configure + start (called when user saves MQTT settings)
- `publish_did_value(ecu, did, name, value)` — checks mqtt_mappings for this datapoint. If enabled, format topic using global format_string or custom_topic. If publish_json, publish json.dumps(value). Else split complex types into scalar sub-topics.
- `publish_ha_discovery(entities, ecus_info)` — publish all enabled HA entity configs. Called at startup and on HA config changes.
- `remove_ha_entity(entity, ecu)` — publish empty payload to remove entity
- `handle_ha_command(topic, payload)` — called when HA sends a command to a writable entity. Parse did/value from topic, push write command to engine.
- Properties: `connected` (bool), `messages_published` (int counter)

Callbacks:
- `on_connect` — subscribe to command topics for writable entities, publish LWT online
- `on_disconnect` — emit status update
- `on_message` — route to handle_ha_command

Store interaction: reads mqtt_host/port/user/password/tls/ca_cert/topic_prefix/format_string/client_id from settings. Reads mqtt_mappings. Reads ha_entities.

### test_mqtt_publisher.py

Tests using mocked paho client (patch paho.Client):
- test_configure_no_host_returns_false
- test_configure_with_host_returns_true
- test_publish_did_value_formatted_topic
- test_publish_did_value_disabled_mapping_skipped
- test_publish_json_mode
- test_connected_property
- test_messages_published_counter

---

### Task 3: Wire MQTT Publisher into Launcher and Server

**Files:**
- Modify: `src/open3e/web/launcher.py`
- Modify: `src/open3e/web/server.py`

### launcher.py changes

After engine creation:
1. Create `publisher = MqttPublisher(store, on_status=on_mqtt_status)`
2. Configure: `loop.run_until_complete(publisher.configure())`
3. If configured successfully, call `publisher.start()`
4. Store on `app.state.mqtt_publisher`
5. Update `on_engine_data` to also call `publisher.publish_did_value()` for did_value messages
6. Define `on_mqtt_status(msg)` that broadcasts mqtt_status via ws_manager

### server.py changes

Update `/api/settings/test-mqtt` and add MQTT reconfigure on settings save:
- When MQTT settings are saved via PATCH, call `publisher.reconfigure()` if publisher exists
- Update `/api/ha/apply-defaults` to actually run smart defaults:
  - Get all datapoints from store
  - For each, call `infer_ha_entity()` 
  - Upsert ha_entity rows
  - Return count of entities created
- When HA settings saved or entities toggled, call `publisher.publish_ha_discovery()` to update HA

---

### Task 4: Authentication Middleware

**Files:**
- Modify: `src/open3e/web/auth.py`
- Create: `tests/web/test_auth.py`
- Modify: `src/open3e/web/server.py`

### auth.py additions

Keep existing `hash_password()` and `verify_password()`.

Add `AuthMiddleware` class (Starlette middleware):
- On each request, check if auth is enabled (read from store or cached flag)
- If disabled, pass through
- If enabled:
  - Allow: `/login`, `/static/*`, `/api/auth/login` without auth
  - Check for session cookie `open3e_session`
  - If valid session token in memory dict, pass through
  - Otherwise redirect to `/login`

Add session management:
- `_sessions: dict[str, float]` — token -> last_access_timestamp
- `create_session()` -> str — generate random token via `secrets.token_hex(32)`, store in dict
- `validate_session(token)` -> bool — check exists and not expired (24h idle timeout)
- `destroy_session(token)` — remove from dict
- `cleanup_expired()` — remove expired sessions

### test_auth.py

Tests:
- test_hash_and_verify_password
- test_verify_wrong_password_fails
- test_create_and_validate_session
- test_expired_session_invalid
- test_destroy_session

### server.py changes

- Add login page route: `GET /login` renders login.html
- Add login handler: `POST /login` — verify password, create session, set cookie, redirect to /
- Add logout: `POST /api/auth/logout` — destroy session, clear cookie
- Mount AuthMiddleware (conditionally — only wraps routes when auth enabled)

---

### Task 5: Apply Smart Defaults Implementation

**Files:**
- Modify: `src/open3e/web/server.py`

Update the `/api/ha/apply-defaults` endpoint to actually run inference:

```python
    @app.post("/api/ha/apply-defaults")
    async def apply_ha_defaults():
        from open3e.web.ha_discovery import infer_ha_entity
        datapoints = await store.get_datapoints()
        created = 0
        for dp in datapoints:
            result = infer_ha_entity(dp["name"], dp.get("codec_type", ""), dp.get("is_writable", False))
            if result:
                await store.upsert_ha_entity(
                    dp["id"], result.get("sub_field"),
                    result["ha_component"], result.get("device_class"),
                    result.get("unit"), result.get("icon"),
                    result.get("entity_name"),
                )
                created += 1
        # Trigger HA discovery publish if publisher exists
        publisher = getattr(app.state, "mqtt_publisher", None)
        if publisher and publisher.connected:
            entities = await store.get_ha_entities(enabled=True)
            ecus = await store.get_ecus()
            topic_prefix = await store.get_setting("mqtt_topic_prefix", "open3e")
            ha_prefix = await store.get_setting("ha_discovery_prefix", "homeassistant")
            publisher.publish_ha_discovery(entities, ecus, topic_prefix, ha_prefix)
        return {"status": "ok", "entities_created": created}
```

---

### Task 6: Final Integration Test and Verification

- [ ] **Step 1: Run all tests**

```bash
pytest tests/web/ -v
```

- [ ] **Step 2: Verify all pages render**

```bash
python -c "
import asyncio
from open3e.web.config_store import ConfigStore
from open3e.web.server import create_app
from httpx import AsyncClient, ASGITransport

async def check():
    store = ConfigStore('/tmp/open3e_plan3_check.db')
    await store.initialize()
    app = create_app(store)
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url='http://test') as c:
        for path in ['/', '/settings', '/datapoints', '/write', '/depict', '/system', '/login']:
            r = await c.get(path)
            print(f'{path}: {r.status_code}')
            assert r.status_code == 200, f'{path} returned {r.status_code}'
    await store.close()
    import os; os.remove('/tmp/open3e_plan3_check.db')

asyncio.run(check())
print('All pages OK')
"
```

- [ ] **Step 3: Verify HA smart defaults on sample data**

```bash
python -c "
import asyncio
from open3e.web.config_store import ConfigStore
from open3e.web.ha_discovery import infer_ha_entity

async def check():
    store = ConfigStore('/tmp/open3e_ha_check.db')
    await store.initialize()
    await store.upsert_ecu(0x680, 'vitocal', 'HPMUMASTER', 'dp.py')
    dp_id = await store.upsert_datapoint(0x680, 268, 'FlowTemperatureSensor', 'O3EComplexType', 9, False)
    result = infer_ha_entity('FlowTemperatureSensor', 'O3EComplexType', False)
    print(f'Inference: {result}')
    assert result['ha_component'] == 'sensor'
    assert result['device_class'] == 'temperature'
    assert result['sub_field'] == 'Actual'
    await store.close()
    import os; os.remove('/tmp/open3e_ha_check.db')

asyncio.run(check())
print('HA defaults OK')
"
```

---

## Summary

After completing Plan 3, the open3e web UI is feature-complete per the design spec:

- **MQTT publisher** with per-datapoint topic mapping, JSON/split mode, TLS support, live reconfiguration
- **HA MQTT auto-discovery** with smart defaults from codec metadata, per-entity override, writable entity command handling
- **Optional authentication** with scrypt password hashing, session cookies, 24h idle timeout
- **Smart defaults** button in HA settings actually populates entity configurations based on datapoint names and codec types

Combined with Plans 1 and 2, the full feature set is:
1. Single-command launcher (`open3e-web`)
2. CAN interface discovery and configuration
3. Priority-based datapoint polling
4. Live dashboard with uPlot charts
5. Datapoints browser with search/filter
6. Write values with confirmation
7. System depiction with live progress
8. MQTT publishing with topic mapping
9. HA auto-discovery with smart defaults
10. System status display
11. Database backup/restore
12. Optional password authentication
13. SQLite configuration persistence
