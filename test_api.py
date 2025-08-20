import requests

BASE_URL = "http://127.0.0.1:8000"

# 1️⃣ Test root endpoint
print("Testing root endpoint...")
resp = requests.get(BASE_URL + "/")
print("Status:", resp.status_code)
print("Response:", resp.json())

# 2️⃣ Add items via query parameter
print("\nAdding items...")
for item in ["apple", "banana", "mango"]:
    resp = requests.get(BASE_URL + "/items/", params={"item": item})
    print(f"Added '{item}' →", resp.json())

# 3️⃣ Fetch individual items by ID
print("\nFetching items by ID...")
for i in range(3):
    resp = requests.get(f"{BASE_URL}/items/{i}")
    print(f"Item {i} →", resp.json())
