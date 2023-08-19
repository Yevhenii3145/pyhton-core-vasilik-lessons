"""
Напишите класс Adder, у которого метод __add__, который генерирует исключение <<NotImplemented>>.
Затем определяет два класса, которые реализуют метод добавления:

a) ListAdder с методом добавления, который возвращает конкатенацию двух своих аргументов списка

б) DictAdder с методом добавления, который возвращает новый словарь с элементами которые есть в двух его аргументах
(Подойдёт любое определение добавления)
"""


class Adder:
    def __add__(self, obj):
        raise NotImplementedError


class ListAdder(Adder):
    def __init__(self, value):
        self.value = value

    def __add__(self, obj):
        return self.value + obj.value


class DictAdder(Adder):
    def __init__(self, value):
        self.value = value

    def __add__(self, obj):
        return {**self.value, **obj.value}


la1 = ListAdder([1, 2])
la2 = ListAdder([3, 4])
print(la1 + la2)  # [1, 2, 3, 4]

da1 = DictAdder({"Irina": 19, "Piter": 12})
da2 = DictAdder({"Roman": 11, "Katia": 25, "Piter": 322})
print(da1 + da2)  # {'Irina': 19, 'Piter': 322, 'Roman': 11, 'Katia': 25}
