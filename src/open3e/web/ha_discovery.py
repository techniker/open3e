"""Home Assistant MQTT discovery — smart defaults and payload builder."""

import fnmatch
from typing import Optional

INFERENCE_RULES = [
    # (name_pattern, codec_types, ha_component, device_class, unit, icon)
    #
    # IMPORTANT: Order matters! More specific patterns must come before generic ones.
    # "CurrentPower" must match Power before Energy. "Percent" must match before generic.

    # --- Instantaneous power (W) — must come BEFORE energy rules ---
    ("*CurrentPower*", ["O3EInt16", "O3EInt32", "O3EComplexType"], "sensor", "power", "W", "mdi:flash"),
    ("*CurrentElectricalPower*", ["O3EInt16", "O3EInt32", "O3EComplexType"], "sensor", "power", "W", "mdi:flash"),
    ("*PowerAc*", ["O3EComplexType", "O3EInt32"], "sensor", "power", "W", "mdi:flash"),
    ("*PowerDc*", ["O3EComplexType", "O3EInt32"], "sensor", "power", "W", "mdi:flash"),
    ("*ThermalPower*", ["O3EComplexType"], "sensor", "power", "W", "mdi:fire"),
    ("*MaximumNominalPower*", ["O3EComplexType", "O3EInt32"], "sensor", "power", "W", "mdi:flash"),
    ("*CurrentMaximumPower*", ["O3EComplexType", "O3EInt32"], "sensor", "power", "W", "mdi:flash"),

    # --- Percent values ---
    ("*Percent*", ["O3EComplexType", "O3EInt8", "O3EByteVal", "O3EInt16"], "sensor", None, "%", "mdi:percent"),
    ("*StateOfCharge*", ["O3EInt8", "O3EByteVal", "O3EInt16", "O3EInt32"], "sensor", "battery", "%", "mdi:battery"),

    # --- Voltage ---
    ("*Voltage*", ["O3EComplexType", "O3EInt16", "O3EInt32", "RawCodec"], "sensor", "voltage", "V", "mdi:flash"),

    # --- Current (Ampere) ---
    ("*StringCurrent*", ["O3EComplexType"], "sensor", "current", "A", "mdi:current-ac"),
    ("*InverterCurrent*", ["O3EComplexType", "O3EInt16"], "sensor", "current", "A", "mdi:current-ac"),

    # --- Photovoltaic ---
    ("*Photovoltaic*Power*", ["O3EComplexType", "O3EInt32"], "sensor", "power", "W", "mdi:solar-panel"),
    ("*Photovoltaic*", ["O3EComplexType", "O3EInt32"], "sensor", None, None, "mdi:solar-panel"),

    # --- Flow rate ---
    ("*Allengra*", ["O3EComplexType"], "sensor", None, "L/h", "mdi:water-pump"),
    ("*FlowRate*", ["O3EComplexType", "O3EInt16", "O3EInt32"], "sensor", None, "L/h", "mdi:water-pump"),

    # --- Pressure ---
    ("*Pressure*", ["O3EComplexType", "O3EInt16"], "sensor", "pressure", "bar", "mdi:gauge"),

    # --- Temperature sensors ---
    ("*Temperature*", ["O3EComplexType", "O3EInt16"], "sensor", "temperature", "\u00b0C", "mdi:thermometer"),
    ("*TemperatureSensor*", ["O3EComplexType"], "sensor", "temperature", "\u00b0C", "mdi:thermometer"),
    ("*Sensor", ["O3EComplexType"], "sensor", "temperature", "\u00b0C", "mdi:thermometer"),

    # --- Energy (cumulative kWh) ---
    ("*EnergyConsumption*", ["O3EComplexType"], "sensor", "energy", "kWh", "mdi:lightning-bolt"),
    ("*GeneratedOutput*", ["O3EComplexType"], "sensor", "energy", "kWh", "mdi:solar-power"),
    ("*Generated*Output*", ["O3EComplexType"], "sensor", "energy", "kWh", "mdi:solar-power"),

    # --- Generic power (W) ---
    ("*Power*", ["O3EInt16", "O3EInt32", "O3EComplexType"], "sensor", "power", "W", "mdi:flash"),

    # --- Generic energy (kWh) — after power rules ---
    ("*Energy*", ["O3EInt32", "O3EInt64", "O3EComplexType"], "sensor", "energy", "kWh", "mdi:lightning-bolt"),

    # --- Flow and water ---
    ("*FlowMeter*", ["O3EInt32", "O3EComplexType"], "sensor", "water", "L", "mdi:water"),

    # --- Frequency ---
    ("*Frequency*", ["O3EInt16", "O3EInt32", "O3EComplexType"], "sensor", "frequency", "Hz", "mdi:sine-wave"),
    ("*Speed*", ["O3EInt16", "O3EInt32"], "sensor", None, "rpm", "mdi:fan"),

    # --- Pumps ---
    ("*Pump*", ["O3EComplexType", "O3EBool", "O3EByteVal"], "sensor", None, None, "mdi:pump"),

    # --- Valves ---
    ("*Valve*", ["O3EComplexType", "O3EInt8", "O3EByteVal"], "sensor", None, "%", "mdi:valve"),

    # --- Setpoints ---
    ("*TemperatureSetpoint*", ["O3EComplexType", "O3EInt16"], "sensor", "temperature", "\u00b0C", "mdi:thermostat"),
    ("*Setpoint*", ["O3EComplexType", "O3EInt16"], "sensor", None, None, "mdi:thermostat"),
    ("*Hysteresis*", ["O3EComplexType"], "sensor", "temperature", "\u00b0C", "mdi:thermostat"),

    # --- Operation modes and states ---
    ("*OperationMode*", ["O3EEnum", "O3EComplexType"], "sensor", None, None, "mdi:cog"),
    ("*OperationState*", ["O3EEnum", "O3EComplexType"], "sensor", None, None, "mdi:toggle-switch"),
    ("*QuickMode*", ["O3EComplexType"], "sensor", None, None, "mdi:flash"),

    # --- Heating curves ---
    ("*HeatingCurve*", ["O3EComplexType"], "sensor", None, None, "mdi:chart-line"),
    ("*CurveAdaption*", ["O3EComplexType"], "sensor", None, None, "mdi:chart-line"),

    # --- Software/Hardware/Identity ---
    ("*Version*", ["O3ESoftVers"], "sensor", None, None, "mdi:information"),
    ("*MacAddress*", ["O3EMacAddr"], "sensor", None, None, "mdi:ethernet"),
    ("*Identification*", ["O3EComplexType", "O3EUtf8", "O3EByteVal"], "sensor", None, None, "mdi:card-account-details"),

    # --- Time and schedule ---
    ("*TimeSchedule*", ["O3EList"], "sensor", None, None, "mdi:clock-outline"),
    ("*Date*", ["O3ESdate"], "sensor", None, None, "mdi:calendar"),
    ("*Time*", ["O3EStime"], "sensor", None, None, "mdi:clock"),

    # --- Catch-all by codec type ---
    ("*", ["O3EEnum"], "sensor", None, None, "mdi:information"),
    ("*", ["O3EBool"], "binary_sensor", None, None, "mdi:toggle-switch"),
    ("*", ["O3EByteVal", "O3EInt8"], "sensor", None, None, "mdi:numeric"),
    ("*", ["O3EInt16", "O3EInt32", "O3EInt64"], "sensor", None, None, "mdi:numeric"),
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
        "object_id": object_id,
        "state_topic": state_topic,
        "device": {
            "identifiers": ["open3e_" + ecu_hex],
            "name": "{} ({})".format(ecu_name, "0x" + ecu_hex),
            "manufacturer": "Viessmann",
            "model": ecu_prop or "Unknown",
        },
        "origin": {
            "name": "open3e",
            "sw_version": sw_version or "0.5.10",
            "support_url": "https://github.com/open3e/open3e",
        },
        "availability": [{
            "topic": topic_prefix + "/LWT",
            "payload_available": "online",
            "payload_not_available": "offline",
        }],
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
