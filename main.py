from fastapi import FastAPI, Header, HTTPException
from typing import Optional

app = FastAPI(title="Header-Protected API", description="Demo API with header authentication")

# Define a reusable header validation function
def verify_api_key(x_api_key: Optional[str]):
    if x_api_key != "secret123":
        raise HTTPException(status_code=401, detail="Invalid or missing API key")


# --- GET Example ---
@app.get("/items")
def get_items(x_api_key: Optional[str] = Header(None)):
    verify_api_key(x_api_key)
    return {"method": "GET", "message": "Fetched all items successfully."}


# --- POST Example ---
@app.post("/items")
def create_item(item: dict, x_api_key: Optional[str] = Header(None)):
    verify_api_key(x_api_key)
    return {"method": "POST", "message": "Item created successfully.", "item": item}


# --- PUT Example ---
@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict, x_api_key: Optional[str] = Header(None)):
    verify_api_key(x_api_key)
    return {"method": "PUT", "message": f"Item {item_id} updated.", "updated_data": item}


# --- DELETE Example ---
@app.delete("/items/{item_id}")
def delete_item(item_id: int, x_api_key: Optional[str] = Header(None)):
    verify_api_key(x_api_key)
    return {"method": "DELETE", "message": f"Item {item_id} deleted."}
