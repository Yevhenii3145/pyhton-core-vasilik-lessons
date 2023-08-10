"""
Асоциация
Это когда один класс содержит другой класс как один из полей. Асоциация описывается
словом "имеет".
Питомец имеет хозяина.
Выделяют два отдельных случая асоциации: композицию и агрегацию.

Композиция
Это когда питомец не существует отдельно от хозяина. Хозяин создаётся при создании питомца
и полностью управляется питомцем.
"""

class Animal:
    def __init__(self, nickname:str, age: int) -> None:
        self.nickname = nickname
        self.age = age

    def get_info(self) ->str:
        return f"It's animal. His name: {self.nickname} and he's {self.age} years old"

class Owner:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone

    def get_info(self) -> str:
        return f"{self.name} {self.phone}"

class Cat(Animal):
    def __init__(self, nickname: str, age: int, name: str, phone: str):
        super(Cat,self).__init__(nickname, age)
        self.owner = Owner(name, phone)

    def sound(self):
        return f"{self.nickname} says Meow"

    def get_info(self) -> str:
        return f"It's cat. His name: {self.nickname} and he's {self.age} years"

cat = Cat("Boris", 4, "Ivan", "0345664224536")
print(cat.owner.get_info()) # Ivan 0345664224536
