from fastapi import FastAPI, Request, Response
from typing import Any, Dict
import json
from datetime import datetime

app = FastAPI(title="One-Endpoint Echo Server")

@app.api_route(
    "/echo/{item_id}",
    methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"]
)
async def echo(item_id: int, request: Request, response: Response, status: int = 200) -> Dict[str, Any]:
    """
    Echo everything about the incoming request.
    Use ?status=<code> to set the response status code (e.g., ?status=201).
    """
    # --- Raw body bytes (safe to read once) ---
    body_bytes = await request.body()
    body_text = body_bytes.decode(errors="replace") if body_bytes else None

    # Try parse JSON from body (if possible)
    body_json = None
    if body_bytes:
        try:
            body_json = json.loads(body_text)  # only if valid JSON
        except Exception:
            body_json = None

    # Try parse form data (handles multipart and urlencoded)
    form_data = None
    files = None
    try:
        form = await request.form()
        # Convert Starlette FormData -> plain dict (UploadFile has .filename)
        form_data = {}
        files = {}
        for k, v in form.multi_items():
            if hasattr(v, "filename"):  # UploadFile
                files.setdefault(k, []).append({"filename": v.filename, "content_type": v.content_type})
            else:
                form_data.setdefault(k, []).append(v)
    except Exception:
        pass  # not form content

    # Basic request info
    info = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "method": request.method,
        "url": str(request.url),
        "path": request.url.path,
        "http_version": request.scope.get("http_version"),
        "client": {
            "host": request.client.host if request.client else None,
            "port": request.client.port if request.client else None,
        },
        "path_params": {"item_id": item_id},
        "query_params": dict(request.query_params),
        "headers": dict(request.headers),
        "cookies": request.cookies,
        "body": {
            "as_json": body_json,
            "as_text": body_text,
            "length_bytes": len(body_bytes) if body_bytes else 0,
        },
        "form": form_data,
        "files": files,
    }

    # Make response reflect chosen status and add a header
    response.status_code = int(status)
    response.headers["x-echo-server"] = "true"

    # --- Print to server console (good for tutorials/demos) ---
    print("\n--- Incoming Request ---------------------------------")
    print(json.dumps(info, indent=2))
    print("Will respond with status:", response.status_code)
    print("------------------------------------------------------\n")

    # Include response meta in the returned payload too
    return {
        "request": info,
        "response": {
            "status_code": response.status_code,
            "headers": dict(response.headers),
        },
    }
