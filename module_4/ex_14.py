numbers = {1, 2, 3, 4, 5}
numbers.remove(2)
print(numbers)

# numbers.remove(20) KeyError: 20

# ошибки не будет даже если нет такого элемента
numbers.discard(20)
print(numbers)

for item in numbers:
    print(item)
