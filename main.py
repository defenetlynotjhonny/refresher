from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Any, Dict
import json
from datetime import datetime

app = FastAPI(title="Echo Web App")

# Mount static files (CSS/JS) and set up templates (HTML)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    # Serves the HTML page
    return templates.TemplateResponse("index.html", {"request": request})

@app.api_route(
    "/echo/{item_id}",
    methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"]
)
async def echo(item_id: int, request: Request, response: Response, status: int = 200):
    """
    Echo everything about the incoming request.
    Use ?status=<code> to select the response status (e.g., ?status=201).
    """
    # Read raw body safely once
    body_bytes = await request.body()
    body_text = body_bytes.decode(errors="replace") if body_bytes else None

    body_json = None
    if body_bytes:
        try:
            body_json = json.loads(body_text)
        except Exception:
            pass

    # Try parse form (covers multipart & urlencoded)
    form_data = None
    files = None
    try:
        form = await request.form()
        form_data = {}
        files = {}
        for k, v in form.multi_items():
            if hasattr(v, "filename"):
                files.setdefault(k, []).append({"filename": v.filename, "content_type": v.content_type})
            else:
                form_data.setdefault(k, []).append(v)
    except Exception:
        pass

    info: Dict[str, Any] = {
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

    response.status_code = int(status)
    response.headers["x-echo-server"] = "true"

    # Log to server console
    print("\n--- Incoming Request ---------------------------------")
    print(json.dumps(info, indent=2))
    print("Will respond with status:", response.status_code)
    print("------------------------------------------------------\n")

    return {
        "request": info,
        "response": {"status_code": response.status_code, "headers": dict(response.headers)},
    }
