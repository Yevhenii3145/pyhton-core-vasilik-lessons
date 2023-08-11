"""
Утиная типизация
Неявная типизация, латентная типизация или утиная типизация (англ. Duck typing) в ООП
языках - определение факта реализации определённого интерфейса объектом без явного
указания или наследования этого интерфейса, а просто реализации полного набора методов.
"""


class Animal:
    def __init__(self, nickname: str, age: int, owner: str = None) -> None:
        self.nickname = nickname
        self.age = age
        self.owner = owner

    def sound(self):
        pass

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


def pet_say(pet: Animal):
    print(pet.sound())


animal = Animal("Chupakabra", 100, "Ivan")
cat = Cat("Boris", 4, "Ivan")
dog = Dog("Rex", 5, "Ivan")

for pet in (animal, cat, dog):
    pet_say(pet)  # None  Boris says Meow  Rex says Woof
