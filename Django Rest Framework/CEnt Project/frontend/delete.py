import requests

product_id = int(input("enter the product id you want to delete."))
if product_id:
    endpoint = f"http://127.0.0.1:8000/products/{product_id}/delete/"

    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code == 204)
