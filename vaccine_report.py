company_name = "VACCINES2U"
vat_number = "VAT GB123456789"
items = []
total_cost = 0
site = input("Vaccination site? ").strip().upper()
while True:
    typ = input("Vaccine type? ").upper()
    if not typ:
        break
    quantity = int(input("Number of vaccines requested? "))
    shipping_cost = float(input("Shipping fee per 100 doses? "))
    total_shipping_cost = shipping_cost / 100 * quantity
    total_cost += total_shipping_cost
    items.append((typ, quantity, total_shipping_cost))
cash_paid = int(input("Cash paid? "))
vat_amount = total_cost * 0.2
change = cash_paid - total_cost
print(f"{company_name:30s}{'SHIPPING ORDER':>25s}")
print(f"{vat_number:30s}{site:>25s}")
print()
print(f"{'Vaccine':25s}{'Qty.':5s}{'Cost':>10s}")
for typ, qty, cost in items:
    print(f"{typ:25s}{qty:5d}{cost:10.2f}")
print()
print(f"{'TOTAL':30s}{total_cost:10.2f}")
print(f"{'VAT INCLUDED IN TOTAL':30s}{vat_amount:10.2f}")
print(f"{'CASH PAID':30s}{cash_paid:10.2f}")
print(f"{'CHANGE':30s}{change:10.2f}")
