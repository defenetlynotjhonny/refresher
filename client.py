import requests
import json

BASE = "http://127.0.0.1:8000"

def call_echo():
    url = f"{BASE}/echo/123"
    params = {
        "status": 201,   # tell the server which status code to use in the response
        "search": "widgets",
        "page": "2",
    }
    headers = {
        "x-api-key": "demo-key-456",
        "X-Custom-Header": "HelloFromClient",
    }
    cookies = {
        "session_id": "abc123",
    }
    payload = {
        "message": "Hello, Echo Server!",
        "items": [1, 2, 3],
        "active": True,
    }

    r = requests.post(url, params=params, headers=headers, cookies=cookies, json=payload)

    print("Status:", r.status_code)
    print("Response headers:", dict(r.headers))
    try:
        data = r.json()
        print("Response JSON:")
        print(json.dumps(data, indent=2))
    except Exception:
        print("Response Text:")
        print(r.text)

if __name__ == "__main__":
    call_echo()
