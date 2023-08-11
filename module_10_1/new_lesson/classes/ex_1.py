class Animal:
    def __init__(self, nickname: str, age: int) -> None:
        self.nickname = nickname
        self.age = age

    def get_info(self) -> str:
        return f"It's animal. His name: {self.nickname} and he's {self.age} years old"


animal = Animal("Rex", 5)
print(animal.nickname)  # Rex
print(animal.age)  # 5
animal.age = 3
print(animal.get_info())  # It's animal. His name: Rex and he's 3 years old
print(animal.age)  # 3

animal_new = Animal("Bob", 11)
print(animal_new.nickname)  # Bob
print(animal_new.age)  # 11

print(animal.age)  # 3
