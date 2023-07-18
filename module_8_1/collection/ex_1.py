"""
Именованные кортежи
Класс collections.namedtuple позволяет создать тип данных,
который ведёт себя как кортеж с возможностью присвоить
каждому элементу имя, по которому далее можна получить доступ
"""

import collections

Point = collections.namedtuple("Point", ["x","y","z"])
p = Point(1,2,3)
print(p.x, p.y, p.z) # 1 2 3

Cat = collections.namedtuple("Cat", ["nickname","age","owner"])
cat = Cat("Mark Antoniy", 3, "Jack")
print(type(cat)) # <class '__main__.Cat'>

print(f"This is a cat {cat.nickname}, {cat.age} age, his owner is: {cat.owner}")

Student = collections.namedtuple("Student", ["name", "age", "gender"])
s = Student("Ivan", 23, "m")
print(Student.__name__) # Student
print(s.name) # Ivan
