"""
Базовые принципы ООП - Наследование

Наследование, является свойством объектов порождать своих потомков. Объект-потомок
автоматичесски унаследывает от отца все поля и методы, может дополнять объекты новыми
полями и изменять (перекрывать) методы отца или дополнять их.
"""


class Animal:
    def __init__(self, nickname: str, age: int) -> None:
        self.nickname = nickname
        self.age = age

    def get_info(self) -> str:
        return f"It's animal. His name: {self.nickname} and he's {self.age} years old"


class Cat(Animal):
    name = ["Cat"]
    test = "GoIT"

    def __init__(self, nickname: str, age: int, owner: str):
        super(Cat, self).__init__(nickname, age)
        self.owner = owner

    def sound(self):
        return f"{self.nickname} says Meow"

    def get_owner(self):
        return f"Cat owner is: {self.owner}"


cat = Cat("Barsik", 3, "Ivan")
print(cat.nickname)  # Barsik
cat.age = 5
cat.nickname = "Byden"
print(cat.age)  # 5
print(cat.get_info())  # It's animal. His name: Byden and he's 5 years old
print(cat.get_owner())  # Cat owner is: Ivan

# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
print(dir(cat))
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__',
# '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'get_info',
# 'name', 'nickname', 'owner', 'sound', 'test']

cat_second = Cat("Jack", 3, "Oksana")
cat.name[0] = "Joe"  # список - изменяемый тип данных
print(f"cat.name: {cat.name}")  # cat.name: ['Joe']
print(f"cat_second.name: {cat_second.name}")  # cat_second.name: ['Joe']
print(f"Cat.name: {Cat.name}")  # Cat.name: ['Joe']

cat.test = "Hello"  # строка - неизменяемый тип
print(f"cat.test: {cat.test}")  # cat.test: Hello
print(f"cat_second.test: {cat_second.test}")  # cat_second.test: GoIT
print(f"Cat.test: {Cat.test}")  # Cat.test: GoIT

Cat.test = "New"
print(f"cat.test: {cat.test}")  # cat.test: Hello
print(f"cat_second.test: {cat_second.test}")  # cat_second.test: New
print(f"Cat.test: {Cat.test}")  # Cat.test: New
