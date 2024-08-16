class Order:

    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        if self.price > order2.price:
            return True
        else:
            return False


odr1 = Order("chips", 20)
odr2 = Order("mango", 50)
print(odr2 > odr1)
