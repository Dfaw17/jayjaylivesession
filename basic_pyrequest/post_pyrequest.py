import json

import requests

data = {
    "name": "Fawwaz",
    "job": "SDET"
}
req = requests.post("https://reqres.in/api/users", json=data)

resp_json = req.json()
print(resp_json)
print(req.elapsed.microseconds / 1000)
print(resp_json.get("name"))
