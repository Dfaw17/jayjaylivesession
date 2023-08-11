import json
import requests
from assertpy import assert_that

param = {
    "page" : "2"
}
req = requests.get("https://reqres.in/api/users", params=param)

resp_json = req.json()
resp_headers = req.headers
latency = req.elapsed.microseconds / 1000
print(latency)

resp_page = resp_json.get("page")
resp_data = resp_json.get("data")
resp_total = resp_json.get("total")
assert_that(resp_page).is_type_of(int)
assert_that(resp_data).is_type_of(list)
assert_that(resp_total).is_equal_to(12)
assert_that(resp_data).is_not_none()
assert_that(req.status_code).is_equal_to(200)
assert_that(latency).is_less_than(1000)