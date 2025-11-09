function safeParseJSON(input, fallback) {
  try {
    if (!input || !input.trim()) return fallback;
    return JSON.parse(input);
  } catch (e) {
    return fallback;
  }
}

function buildQueryString(obj) {
  const qs = new URLSearchParams();
  for (const [k, v] of Object.entries(obj || {})) {
    // Convert non-strings to string
    qs.append(k, typeof v === "string" ? v : JSON.stringify(v));
  }
  return qs.toString();
}

async function sendRequest() {
  const out = document.getElementById("output");
  out.textContent = "Sending…";

  const itemId = document.getElementById("itemId").value || "123";
  const statusCode = document.getElementById("statusCode").value || "200";

  const queryJson = safeParseJSON(document.getElementById("queryJson").value, {});
  const headersJson = safeParseJSON(document.getElementById("headersJson").value, {});
  const bodyJson = safeParseJSON(document.getElementById("bodyJson").value, null);

  // Always include requested status code as query param
  const params = { status: Number(statusCode), ...queryJson };
  const qs = buildQueryString(params);

  const url = `/echo/${encodeURIComponent(itemId)}?${qs}`;

  const fetchOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...headersJson, // user-provided custom headers (subject to browser restrictions)
    },
    credentials: "same-origin", // send cookies for same-origin requests
    body: bodyJson ? JSON.stringify(bodyJson) : null,
  };

  try {
    const res = await fetch(url, fetchOptions);
    const txt = await res.text();
    // Try JSON first; if not JSON, show raw text
    let payload;
    try {
      payload = JSON.parse(txt);
    } catch {
      payload = { raw: txt };
    }

    const display = {
      client_view: {
        requested_url: url,
        method: fetchOptions.method,
        sent_headers: fetchOptions.headers,
        sent_body: bodyJson,
        requested_status: statusCode
      },
      server_response: {
        status: res.status,
        statusText: res.statusText,
        headers: Object.fromEntries(res.headers.entries()),
        body: payload
      }
    };

    out.textContent = JSON.stringify(display, null, 2);
  } catch (err) {
    out.textContent = `Error: ${err}`;
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("sendBtn").addEventListener("click", sendRequest);
});
