import requests

endpoint = "http://localhost:8000/api/"


# get_response = requests.get(endpoint, params={"abc": 123})
get_response = requests.post(
    endpoint, json={"name": "Alice", "message": "Hello from POST!"}
)


# print(get_response.text)  # print raw response text
# print(get_response.status_code)
# print(get_response.json())

# if http request -> html doc
# if REST api http request -> JSON or XML

endpoint2 = "http://localhost:8000/api/api_model/"

get_response = requests.get(endpoint2)
try:
    print(get_response.json())
except:
    print("Not JSON! Raw response:")
endpoint3 = "http://localhost:8000/api/drf_view/"

get_response = requests.get(endpoint3)
try:
    print(get_response.json())
except:
    print("Not JSON! Raw response:")
