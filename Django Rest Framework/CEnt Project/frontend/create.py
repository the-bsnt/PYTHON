import requests

endpoint = "http://127.0.0.1:8000/products/"
get_response = requests.post(
    endpoint,
    json={
        "title": "product37",
        "content": "Electronic Product",
        "price": 5999,
    },
)
print(get_response.json())
