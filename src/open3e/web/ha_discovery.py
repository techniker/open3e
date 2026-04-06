"""Home Assistant MQTT discovery — smart defaults and payload builder."""

import fnmatch
from typing import Optional

INFERENCE_RULES = [
    # (name_pattern, codec_types, ha_component, device_class, unit, icon)
    ("*Temperature*", ["O3EComplexType", "O3EInt16"], "sensor", "temperature", "\u00b0C", "mdi:thermometer"),
    ("*Pressure*", ["O3EComplexType", "O3EInt16"], "sensor", "pressure", "bar", "mdi:gauge"),
    ("*Energy*", ["O3EInt32", "O3EInt64"], "sensor", "energy", "kWh", "mdi:lightning-bolt"),
    ("*FlowMeter*", ["O3EInt32"], "sensor", "water", "L", "mdi:water"),
    ("*Power*", ["O3EInt16", "O3EInt32"], "sensor", "power", "W", "mdi:flash"),
    ("*OperationMode*", ["O3EEnum"], "select", None, None, "mdi:cog"),
    ("*OperationState*", ["O3EEnum"], "select", None, None, "mdi:toggle-switch"),
    ("*Setpoint*", ["O3EComplexType", "O3EInt16"], "number", "temperature", "\u00b0C", "mdi:thermostat"),
    ("*Pump*", ["O3EBool"], "binary_sensor", None, None, "mdi:pump"),
]


def _humanize(name: str) -> str:
    """Convert CamelCase DID name to human-readable: 'FlowTemperatureSensor' -> 'Flow Temperature Sensor'."""
    import re
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', name)


def infer_ha_entity(dp_name: str, codec_type: str, is_writable: bool) -> Optional[dict]:
    """Infer HA entity config from datapoint name and codec type.

    Returns dict with: ha_component, device_class, unit, icon, sub_field, entity_name
    Returns None if no rule matches.
    """
    for pattern, codec_types, component, device_class, unit, icon in INFERENCE_RULES:
        if fnmatch.fnmatch(dp_name, pattern) and codec_type in codec_types:
            sub_field = "Actual" if codec_type == "O3EComplexType" else None
            # Writable setpoints use "number" component
            if is_writable and component == "sensor":
                component = "number"
            return {
                "ha_component": component,
                "device_class": device_class,
                "unit": unit,
                "icon": icon,
                "sub_field": sub_field,
                "entity_name": _humanize(dp_name),
            }
    return None


def build_discovery_payload(
    entity: dict, ecu_address: int, ecu_name: str, ecu_prop: str,
    topic_prefix: str = "open3e", ha_prefix: str = "homeassistant",
    sw_version: str = ""
) -> tuple:
    """Build HA MQTT discovery topic and payload.

    Args:
        entity: dict with keys from ha_entities table (ha_component, device_class, unit, icon,
                entity_name, sub_field, did, dp_name, ecu_address)
        ecu_address: ECU address integer
        ecu_name: ECU name string
        ecu_prop: device property string (e.g., "HPMUMASTER")
        topic_prefix: MQTT topic prefix
        ha_prefix: HA discovery prefix
        sw_version: software version string

    Returns: (topic_str, payload_dict)
    """
    component = entity.get("ha_component") or entity.get("entity_type") or "sensor"
    did = entity["did"]
    sub = entity.get("sub_field") or ""
    ecu_hex = format(ecu_address, "03x")

    # Use unique_id from DB if available, otherwise build it
    object_id = entity.get("unique_id")
    if not object_id:
        obj_parts = ["open3e", ecu_hex, str(did)]
        if sub:
            obj_parts.append(sub.lower())
        object_id = "_".join(obj_parts)

    # State topic — must match the actual MQTT data publish topic
    dp_name = entity.get("dp_name") or entity.get("name") or "DID_" + str(did)
    base_topic = "{}/{}_{}".format(topic_prefix, did, dp_name)

    # For ComplexType sensors (unique_id ending in _actual), the split-mode data
    # goes to .../Actual sub-topic. Detect from unique_id.
    is_actual = object_id.endswith("_actual")
    if is_actual:
        state_topic = base_topic + "/Actual"
    elif sub:
        state_topic = base_topic + "/" + sub
    else:
        state_topic = base_topic

    # Discovery topic
    topic = "{}/{}/{}/config".format(ha_prefix, component, object_id)

    payload = {
        "name": entity.get("entity_name") or entity.get("name") or dp_name,
        "unique_id": object_id,
        "state_topic": state_topic,
        "device": {
            "identifiers": ["open3e_" + ecu_hex],
            "name": "{} ({})".format(ecu_name, "0x" + ecu_hex),
            "manufacturer": "Viessmann",
            "model": ecu_prop or "Unknown",
        },
    }
    if sw_version:
        payload["device"]["sw_version"] = sw_version
    if entity.get("device_class"):
        payload["device_class"] = entity["device_class"]
    if entity.get("unit"):
        payload["unit_of_measurement"] = entity["unit"]
    if entity.get("icon"):
        payload["icon"] = entity["icon"]

    # Writable entities get a command topic
    if component in ("number", "select"):
        payload["command_topic"] = state_topic + "/set"

    return (topic, payload)


def build_removal_payload(entity: dict, ecu_address: int, ha_prefix: str = "homeassistant") -> tuple:
    """Build empty payload to remove entity from HA."""
    component = entity.get("ha_component") or entity.get("entity_type") or "sensor"
    did = entity["did"]
    sub = entity.get("sub_field") or ""
    ecu_hex = format(ecu_address, "03x")

    obj_parts = ["open3e", ecu_hex, str(did)]
    if sub:
        obj_parts.append(sub.lower())
    object_id = "_".join(obj_parts)

    topic = "{}/{}/{}/config".format(ha_prefix, component, object_id)
    return (topic, b"")
