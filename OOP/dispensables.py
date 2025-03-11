class Order:
    def __init__(self, product, amount):
        self.product = product
        self.amount = amount

    def get_amount(self):
        return self.amount

class Product:
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price

# amount
a = Order.get_amount()
# discount factor
b = 1
if a > 10:
    b = 0.9
# discounted price
c = Product.get_price() * b
# order sum price
d = a * c
