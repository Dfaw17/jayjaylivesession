import requests
import json

# ====================================== CREATE ======================================
data = {
    "name": "Fawwaz",
    "job": "SDET"
}
req = requests.post("https://reqres.in/api/users", json=data)
print(req.json())
id = req.json().get("id")

# ====================================== UPDATE ======================================
data = {
    "name": "Maulana",
    "job": "QA Engineer"
}
req = requests.put(f"https://reqres.in/api/users/{id}", json=data)
print(req.json())

# ====================================== DELETE ======================================
req = requests.delete(f"https://reqres.in/api/users/{id}")
print(req.status_code)