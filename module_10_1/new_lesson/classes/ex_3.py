"""
Базовые принципы ООП - Полиморфизм

Полиморфизм - это свойство родственных объектов (тоесть объектов, которые имеют одного общего отца)
решать похожие по содержанию проблемы разными способами.
"""


class Animal:
    def __init__(self, nickname: str, age: int) -> None:
        self.nickname = nickname
        self.age = age

    def get_info(self) -> str:
        return f"It's animal. His name: {self.nickname} and he's {self.age} years old"


class Cat(Animal):

    def __init__(self, nickname: str, age: int, owner: str):
        super(Cat, self).__init__(nickname, age)
        self.owner = owner

    def sound(self):
        return f"{self.nickname} says Meow"

    def get_info(self) -> str:
        return f"It's cat. His name: {self.nickname} and he's {self.age} years old"


class Dog(Animal):

    def __init__(self, nickname: str, age: int, owner: str):
        super(Dog, self).__init__(nickname, age)
        self.owner = owner

    def sound(self):
        return f"{self.nickname} says Woof"

    def get_info(self) -> str:
        return f"It's dog. His name: {self.nickname} and he's {self.age} years old"


cat = Cat("Boris", 4, "Ivan")
dog = Dog("Rex", 3, "Ivan")
print("-" * 10)
print(isinstance(dog, Animal))  # True
print(isinstance(dog, Cat))  # False
print(isinstance(dog, Dog))  # True
print("-" * 10)
print(type(dog) is Animal)  # False
print(type(dog) is Dog)  # True
print("-" * 10)
print(dog.get_info())  # It's dog. His name: Rex and he's 3 years old

for el in (cat, dog):
    if type(el) is Dog:
        # Rex says Woof | It's dog. His name: Rex and he's 3 years old
        print(f"{el.sound()} | {el.get_info()}")

for el in (cat, dog):
    if type(el) is Cat:
        # Boris says Meow | It's cat. His name: Boris and he's 4 years old
        print(f"{el.sound()} | {el.get_info()}")
