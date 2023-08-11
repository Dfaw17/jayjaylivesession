import requests
import json

data = {
    "name": "Fawwaz",
    "job": "SDET"
}
req = requests.post("https://reqres.in/api/users", json=data)
print(req.json())
id = req.json().get("id")

data = {
    "name": "Maulana",
    "job": "QA Engineer"
}
req = requests.put(f"https://reqres.in/api/users/{id}", json=data)
print(req.json())
print(req.status_code)