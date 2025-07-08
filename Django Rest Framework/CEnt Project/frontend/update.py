import requests

endpoint = "http://127.0.0.1:8000/products/3/update"
data = {
    "title": "Renerv",
    "content": "Methlycobalamin Sublingual Tablets",
    "price": 216,
}
get_response = requests.put(endpoint, json=data)
print(get_response.json())
