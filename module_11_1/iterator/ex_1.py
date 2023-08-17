"""
Протокол итератора в Python реализованный методом __iter__.Этот метод должен возвращать итератор.
Итератором может быть любой объект, кторый имеет метод __next__, который при каждом вызове возвращает значение.
Чтобы создать итератор, достаточно реализовать метод __next__.
"""
from random import randint


class RandIterator:
    def __init__(self, start, end, quantity):
        self.start = start
        self.end = end
        self.quantity = quantity
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.quantity:
            raise StopIteration
        else:
            return randint(self.start, self.end)


my_random_list = RandIterator(1, 20, 5)

print(my_random_list)  # <__main__.RandIterator object at 0x0000019E87360890>
for ran in my_random_list:
    print(ran, end=" ")  # 17 11 18 14 11
