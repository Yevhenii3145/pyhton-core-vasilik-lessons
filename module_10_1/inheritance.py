class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __repr__(self):
        return f"{self.name} is {self.age} years old"

    def about_cat(self):
        return f"{self.name} is {self.age} years old"

    # @staticmethod
    # @classmethod
    def speak(self, sound):
        return f"{self.name} said {sound}"

class SfinksCat(Cat):
    pass

class KitPes(Cat):
    pass

class PersianCat(Cat):
    pass




my_cat = Cat("kit-pes", 1)
print(my_cat.about_cat())  # kit-pes is 1 years old
print(my_cat) # kit-pes is 1 years old

sfinks = SfinksCat("Sfinks", 3)
kit_pes = KitPes("Kit-Pes", 2)
persian = PersianCat("Persian", 6)

print(sfinks) # Sfinks is 3 years old
print(kit_pes) # Kit-Pes is 2 years old
print(persian) # Persian is 6 years old

print(isinstance(sfinks, Cat)) # True
print(isinstance(sfinks, SfinksCat)) # True
