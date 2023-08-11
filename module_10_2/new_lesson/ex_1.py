# Реализовать класс для магазина
class ProductInStore:
    # price = 5.55
    # name = "new product"

    def __init__(self, price=5.55, name="new product"):
        self.price = price
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_name(self, name):
        self.name = name

    def set_stock(self, qty):
        self.qty_in_stock = qty


lego = ProductInStore(1350, "Train")
lego.set_stock(6)
print(lego.name, lego.price, lego.qty_in_stock)  # Train 1350 6
lego.set_name("Harry Potter")
lego.set_price(5000)
lego.set_stock(10)
print(lego.name, lego.price, lego.qty_in_stock)  # Harry Potter 5000 10
