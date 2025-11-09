import requests

BASE_URL = "http://127.0.0.1:8000"
HEADERS = {"x-api-key": "secret123"}  # required header


def test_get():
    r = requests.get(f"{BASE_URL}/items", headers=HEADERS)
    print("GET:", r.status_code, r.json())


def test_post():
    data = {"name": "Apple", "price": 1.99}
    r = requests.post(f"{BASE_URL}/items", json=data, headers=HEADERS)
    print("POST:", r.status_code, r.json())


def test_put():
    data = {"price": 2.49}
    r = requests.put(f"{BASE_URL}/items/1", json=data, headers=HEADERS)
    print("PUT:", r.status_code, r.json())


def test_delete():
    r = requests.delete(f"{BASE_URL}/items/1", headers=HEADERS)
    print("DELETE:", r.status_code, r.json())


if __name__ == "__main__":
    test_get()
    test_post()
    test_put()
    test_delete()
