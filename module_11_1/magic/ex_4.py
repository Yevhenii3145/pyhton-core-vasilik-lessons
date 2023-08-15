# Методы __repr__ и __str__
class Car:
    store_name = "GoIT"

    def __init__(self, year, mark, model, color):
        self.year = year
        self.mark = mark
        self.model = model
        self.color = color

    def __str__(self):
        return f"{self.store_name}: {self.mark}.{self.model}: {self.year}, {self.color}"

    # если это представить в виде обычно функции
    def info(self):
        return f"{self.store_name}: {self.mark}.{self.model}: {self.year}, {self.color}"


car = Car(2019, "Tesla", "Model X", "White")
print(car)  # GoIT: Tesla.Model X: 2019, White  # print(str(car))
print(car.info())  # GoIT: Tesla.Model X: 2019, White
