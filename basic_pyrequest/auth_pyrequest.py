import requests

# ====================================== CREATE ======================================
data = {
    "name": "Fawwaz",
    "gender": "male",
    "email": "dfawwaz19@gmail.com",
    "status": "active"
}
head = {
    "Authorization" : "Bearer 38cebe5affdc6038017ae850b112f50d15613c3f40d9d2a5d7bfd75f6218fcc2"
}
req = requests.post("https://gorest.co.in/public/v2/users", json=data, headers=head)
id = req.json().get("id")
print(req.json())

# ====================================== DELETE ======================================
head = {
    "Authorization" : "Bearer 38cebe5affdc6038017ae850b112f50d15613c3f40d9d2a5d7bfd75f6218fcc2"
}
req = requests.delete(f"https://gorest.co.in/public/v2/users/{id}", headers=head)
print(req.status_code)