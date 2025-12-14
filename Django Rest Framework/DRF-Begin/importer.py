import csv
from redis_intro.models import Products


def import_data():
    with open("products.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        products = []

        for row in reader:
            products.append(
                Products(
                    name=row["name"],
                    hs_code=row["hs_code"],
                    price=row["price"],
                )
            )

        Products.objects.bulk_create(products)
