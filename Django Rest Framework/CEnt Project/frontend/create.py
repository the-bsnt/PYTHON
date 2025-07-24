import requests

headers = {"Authorization": "Bsnt 0bf311a74fc04d0d7cf8307636122ed9df512592"}


endpoint = "http://127.0.0.1:8000/products/"
get_response = requests.post(
    endpoint,
    json={
        "title": "product40",
        "email": "this@gmail.com",
        "content": "wire Gause",
        "price": 500,
    },
    headers=headers,
)
print(get_response.json())
