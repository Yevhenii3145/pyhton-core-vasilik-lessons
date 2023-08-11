"""
Агрегация
Это когда экземпляр хозяина создаётся где-то в другом месте кода, и передаётся в
конструктор питомца как параметр
"""


class Animal:
    def __init__(self, nickname: str, age: int) -> None:
        self.nickname = nickname
        self.age = age

    def get_info(self) -> str:
        return f"It's animal. His name: {self.nickname} and he's {self.age} years old"


class Owner:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def get_info(self) -> str:
        return f"{self.name} {self.phone}"


class Cat(Animal):
    def __init__(self, nickname: str, age: int, owner: Owner):
        super(Cat, self).__init__(nickname, age)
        self.owner = owner

    def sound(self):
        return f"{self.nickname} says Meow"

    def get_info(self) -> str:
        return f"It's cat. His name: {self.nickname} and he's {self.age} years"


owner = Owner("Ivan", "767676767676")
cat = Cat("Boris", 4, owner)
print(cat.owner.get_info())  # Ivan 767676767676
