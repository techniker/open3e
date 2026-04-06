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
