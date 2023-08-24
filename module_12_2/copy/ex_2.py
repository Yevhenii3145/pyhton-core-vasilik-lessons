# Под капотом функции copy, deepcopy просто вызывают методы __copy__, __deepcopy__.
from collections import UserList
from copy import copy, deepcopy


class CopyList(UserList):
    def __init__(self, *data):
        super().__init__()
        self.data = list(data)

    def __copy__(self):
        n = CopyList()
        n.data = self.data
        return n

    def __deepcopy__(self, memodict={}):
        n = CopyList()
        # memodict хранит id объектов как ключи, и сами объекты как значения
        memodict[id(self)] = n
        for el in self.data:
            n.append(deepcopy(el, memodict))
        return n


data = CopyList([1, 2, 3, 4])
data_copy = copy(data)
data_deep = deepcopy(data)


print(id(data), data)  # 1955978366288 [[1, 2, 3, 4]]
print(id(data_copy), data_copy)  # 1955978615248 [[1, 2, 3, 4]]
print(id(data_deep), data_deep)  # 1955978623376 [[1, 2, 3, 4]]

print(id(data[0]), data[0])  # 1676616690752 [1, 2, 3, 4]
print(id(data_copy[0]), data_copy[0])  # 1676616690752 [1, 2, 3, 4]
print(id(data_deep[0]), data_deep[0])  # 1676616604480 [1, 2, 3, 4]
