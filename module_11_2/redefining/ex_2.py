# Логические операции
class Car:
    def __init__(self, year, mark, model, color, price):
        self.year = year
        self.mark = mark
        self.model = model
        self.color = color
        self.price = price

    def __str__(self):
        return f"{self.mark}.{self.model}: {self.year}, {self.color} and price is: {self.price}"

    def __eq__(self, other):
        print("__eq__")
        return self.price == other.price

    def __ne__(self, other):
        print("__ne__")
        return self.price != other.price

    def __lt__(self, other):
        print("__lt__")
        return self.price < other.price

    def __gt__(self, other):
        print("__gt__")
        return self.price > other.price

    def __le__(self, other):
        print("__le__")
        return self.price <= other.price

    def __ge__(self, other):
        print("__ge__")
        return self.price >= other.price


car_a = Car(2021, "Ford", "Fusion", "Black", 20_000)
car_b = Car(2019, "Toyota", "Camry", "White", 28_000)
print(car_a)  # Ford.Fusion: 2021, Black and price is: 20000
print(car_b)  # Toyota.Camry: 2019, White and price is: 20000
print(car_a == car_b)  # __eq__ True
print(car_a != car_b)  # __ne__ True
print(car_a < car_b)  # __lt__ True
print(car_a > car_b)  # __gt__ False
print(car_a >= car_b)  # __ge__ False
print(car_a <= car_b)  # __le__ True
