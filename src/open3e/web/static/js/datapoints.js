/* open3e web UI — datapoints browser */

var wsApi = null;

document.addEventListener("DOMContentLoaded", function () {
    wsApi = openWebSocket();
    wsApi.onDidValue = handleDidValue;

    wsApi.socket.addEventListener("open", function () {
        wsApi.subscribe("*");
    });
});

function formatValue(value) {
    if (value === null || value === undefined) { return "--"; }
    if (typeof value !== "object") { return String(value); }
    if (value.Actual !== undefined) { return String(value.Actual); }
    var keys = Object.keys(value);
    for (var i = 0; i < keys.length; i++) {
        if (typeof value[keys[i]] === "number") {
            return String(value[keys[i]]);
        }
    }
    return JSON.stringify(value);
}

function handleDidValue(msg) {
    var cellId = "val-" + msg.ecu + "_" + msg.did;
    var cell = document.getElementById(cellId);
    if (!cell) { return; }
    var formatted = formatValue(msg.value);
    cell.textContent = formatted;
    cell.title = typeof msg.value === "object" ? JSON.stringify(msg.value, null, 2) : String(msg.value);
    cell.classList.remove("flash-green");
    // Force reflow so the animation restarts
    void cell.offsetWidth;
    cell.classList.add("flash-green");
}

function filterTable() {
    var search = document.getElementById("dp-search").value.toLowerCase();
    var ecuFilter = document.getElementById("dp-ecu-filter").value;
    var prioFilter = document.getElementById("dp-prio-filter").value;

    var rows = document.querySelectorAll("#dp-table tbody tr");
    rows.forEach(function (row) {
        var name = (row.dataset.name || "").toLowerCase();
        var did = (row.dataset.did || "").toLowerCase();
        var ecu = row.dataset.ecu || "";
        var priority = row.dataset.priority || "";

        var matchSearch = !search || name.indexOf(search) !== -1 || did.indexOf(search) !== -1;
        var matchEcu = !ecuFilter || ecu === ecuFilter;
        var matchPrio = !prioFilter || priority === prioFilter;

        row.style.display = (matchSearch && matchEcu && matchPrio) ? "" : "none";
    });
}

async function setPriority(dpId, priority) {
    try {
        await apiCall("/api/datapoints/" + dpId, "PATCH", { poll_priority: parseInt(priority, 10) });
        // Update data-priority attribute on the row for filter consistency
        var row = document.querySelector("tr[data-dp-id='" + dpId + "']");
        if (row) { row.dataset.priority = priority; }
    } catch (e) {
        // error toast already shown by apiCall
    }
}

async function togglePolling(dpId, enabled) {
    try {
        await apiCall("/api/datapoints/" + dpId, "PATCH", { poll_enabled: enabled });
    } catch (e) {
        // Revert toggle on failure
        var toggle = document.getElementById("poll-" + dpId);
        if (toggle) { toggle.checked = !enabled; }
    }
}

async function bulkSetPriority() {
    var priority = document.getElementById("bulk-priority-select").value;
    if (!priority) {
        showToast("Please select a priority value.", "warning");
        return;
    }
    var checked = document.querySelectorAll(".dp-check:checked");
    if (checked.length === 0) {
        showToast("No datapoints selected.", "warning");
        return;
    }
    var promises = [];
    checked.forEach(function (cb) {
        promises.push(setPriority(cb.value, priority));
    });
    await Promise.all(promises);
    // Update the inline selects in the table
    checked.forEach(function (cb) {
        var sel = document.getElementById("prio-sel-" + cb.value);
        if (sel) { sel.value = priority; }
        var row = document.querySelector("tr[data-dp-id='" + cb.value + "']");
        if (row) { row.dataset.priority = priority; }
    });
    showToast("Priority updated for " + checked.length + " datapoint(s).", "success");
}

async function bulkSetPoll(enabled) {
    var checked = document.querySelectorAll(".dp-check:checked");
    if (checked.length === 0) {
        showToast("No datapoints selected.", "warning");
        return;
    }
    var promises = [];
    checked.forEach(function (cb) {
        promises.push(togglePolling(cb.value, enabled));
    });
    await Promise.all(promises);
    // Update the inline switches
    checked.forEach(function (cb) {
        var sw = document.getElementById("poll-" + cb.value);
        if (sw) { sw.checked = enabled; }
    });
    showToast("Polling " + (enabled ? "enabled" : "disabled") + " for " + checked.length + " datapoint(s).", "success");
}

async function saveAndApply() {
    var btn = document.getElementById("btn-save-apply");
    var status = document.getElementById("save-status");
    btn.disabled = true;
    status.textContent = "Applying...";
    status.className = "ms-2 small text-warning";
    try {
        var result = await apiCall("/api/engine/reload-schedule", "POST");
        status.textContent = "Applied: " + result.polling + " datapoints polling";
        status.className = "ms-2 small text-success";
        showToast("Engine schedule reloaded: " + result.polling + " datapoints active", "success");
    } catch (e) {
        status.textContent = "Failed to apply";
        status.className = "ms-2 small text-danger";
    }
    btn.disabled = false;
}

function toggleSelectAll(master) {
    var checkboxes = document.querySelectorAll(".dp-check");
    checkboxes.forEach(function (cb) {
        // Only toggle visible rows
        var row = cb.closest("tr");
        if (!row || row.style.display === "none") { return; }
        cb.checked = master.checked;
    });
}
