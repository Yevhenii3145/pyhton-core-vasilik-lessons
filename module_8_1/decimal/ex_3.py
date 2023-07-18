# Создание Decimal из действительных чисел

from decimal import Decimal

num_1 = 1.37
num_2 = 1.5

first = Decimal.from_float(num_1)
second = Decimal.from_float(num_2)
print(first, second) # 1.37000000000000010658141036401502788066864013671875 1.5

first = Decimal(str(num_1))
second = Decimal(str(num_2))
print(first, second) # 1.37 1.5

first = Decimal(num_1)
second = Decimal(num_2)
print(first, second) # 1.37000000000000010658141036401502788066864013671875 1.5
