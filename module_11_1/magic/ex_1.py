class Product:
    def __init__(self, name, price):
        print("It's __init__")
        self.name = name
        self.price = price


product = Product("Car", 15_000)  # It's __init__
print(product.price)  # 15000
print(product.name)  # Car
