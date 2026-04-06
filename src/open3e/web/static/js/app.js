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

/**
 * Open a WebSocket connection to the server and return a control object.
 * @returns {object} API object with subscribe, write, close methods and callback properties
 */
function openWebSocket() {
    var protocol = window.location.protocol === "https:" ? "wss://" : "ws://";
    var url = protocol + window.location.host + "/ws";

    var api = {
        socket: null,
        _closed: false,
        onDidValue: null,
        onEngineState: null,
        onCanStatus: null,
        onMqttStatus: null,
        onDepictProgress: null,
        onDepictComplete: null,
        onWriteResult: null,
        onError: null,
    };

    function connect() {
        var ws = new WebSocket(url);
        api.socket = ws;

        ws.onmessage = function (event) {
            var msg;
            try {
                msg = JSON.parse(event.data);
            } catch (e) {
                return;
            }
            switch (msg.type) {
                case "did_value":
                    if (api.onDidValue) { api.onDidValue(msg); }
                    break;
                case "engine_state":
                    if (api.onEngineState) { api.onEngineState(msg); }
                    break;
                case "can_status":
                    if (api.onCanStatus) { api.onCanStatus(msg); }
                    break;
                case "mqtt_status":
                    if (api.onMqttStatus) { api.onMqttStatus(msg); }
                    break;
                case "depict_progress":
                    if (api.onDepictProgress) { api.onDepictProgress(msg); }
                    break;
                case "depict_complete":
                    if (api.onDepictComplete) { api.onDepictComplete(msg); }
                    break;
                case "write_result":
                    if (api.onWriteResult) { api.onWriteResult(msg); }
                    break;
                case "error":
                    if (api.onError) { api.onError(msg); }
                    break;
                default:
                    break;
            }
        };

        ws.onclose = function () {
            if (!api._closed) {
                setTimeout(connect, 3000);
            }
        };
    }

    api.subscribe = function (dids) {
        if (api.socket && api.socket.readyState === WebSocket.OPEN) {
            api.socket.send(JSON.stringify({ type: "subscribe", dids: dids }));
        }
    };

    api.write = function (ecu, did, value, sub) {
        if (api.socket && api.socket.readyState === WebSocket.OPEN) {
            api.socket.send(JSON.stringify({
                type: "write",
                ecu: ecu,
                did: did,
                value: value,
                sub: sub,
            }));
        }
    };

    api.close = function () {
        api._closed = true;
        if (api.socket) {
            api.socket.close();
        }
    };

    connect();
    return api;
}

/**
 * Update sidebar status indicator dots based on an engine state message.
 * @param {object} msg - Message with a "state" property
 */
function updateStatusIndicators(msg) {
    var state = msg.state;
    var dot = document.getElementById("engine-status-dot");
    var label = document.getElementById("engine-status-label");
    var canDot = document.getElementById("can-status-dot");

    if (!dot || !label) { return; }

    dot.className = "status-dot";
    if (canDot) { canDot.className = "status-dot"; }

    switch (state) {
        case "polling":
            dot.classList.add("status-green");
            label.textContent = "Polling";
            if (canDot) { canDot.classList.add("status-green"); }
            break;
        case "connecting":
            dot.classList.add("status-amber");
            label.textContent = "Connecting";
            break;
        case "paused":
            dot.classList.add("status-amber");
            label.textContent = "Paused";
            break;
        case "idle":
            dot.classList.add("status-gray");
            label.textContent = "Idle";
            if (canDot) { canDot.classList.add("status-gray"); }
            break;
        default:
            dot.classList.add("status-gray");
            label.textContent = state || "Unknown";
            break;
    }
}
