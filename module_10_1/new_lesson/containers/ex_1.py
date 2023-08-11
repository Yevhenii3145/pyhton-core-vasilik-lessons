from collections import UserList
from random import randint


class MyList(UserList):  # расширяем функционал
    _info = "This  is my list class"

    def get_positive(self):
        return list(filter(lambda x: x >= 0, self.data))

    def get_negative(self):
        return list(filter(lambda x: x < 0, self.data))

    def append_external(self, item) -> None:
        self.append(item)
        print("Hello")

    def get_info(self):
        return self._info


r = []
for _ in range(0, 20):
    r.append(randint(-5, 5))

result = MyList(r)
# [-4, -5, -2, 2, 5, 5, -4, 5, 4, 1, 4, -5, 1, -1, -2, -3, 0, 5, 0, -5]
print(result)
print(type(result))  # <class '__main__.MyList'>
print(result.get_negative())  # [-2, -3, -5, -5, -2]
print(result.get_positive())  # [0, 2, 1, 1, 1, 1, 0, 1, 2, 0, 3, 0, 1, 0, 1]
print(result.get_info())  # This  is my list class
result.append_external(5555)  # Hello
# [0, 2, 1, -2, 1, -3, 1, 1, 0, 1, -5, 2, 0, -5, -2, 3, 0, 1, 0, 1, 5555]
print(result)
