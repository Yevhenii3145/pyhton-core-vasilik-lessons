# Методы getitem и setitem
from collections import UserList


class PositiveNumber(UserList):
    def __init__(self, data=[]):
        super(PositiveNumber, self).__init__()
        self.data = [el for el in list(filter(lambda x: x > 0, data))]

    def __getitem__(self, index):
        if index is None:
            return self.data
        return self.data[index]

    def __setitem__(self, key, value):
        if value > 0 and key < len(self.data):
            self.data[key] = value

    def append(self, item):
        if item > 0:
            super().append(item)


nums = PositiveNumber([2, -4, 5])
print(nums)  # [2, 5]
print(nums[0])  # 2
print(nums[1])  # 5
print(nums[None])  # [2, 5]
nums[1] = -1
nums[1] = 3
print(nums)  # [2, 3]
nums.append(-5)  # отрицательное значение не можем добавить
print(nums)  # [2, 3]

nums.append(5)
print(nums)  # [2, 3, 5]
