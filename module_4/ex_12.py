# сеты или множества
empty_set = set()
numbers = {1, 2, 3, 4, 5}
print(numbers)
print(type(numbers))

# передаем любую итеррируемую последовательность
print(set("qwerty"))
print(433 in numbers)  # False
print(1 in numbers)

# test = {1, 4, "fff", [4, 6]} TypeError: unhashable type: 'list'

# помещаем только хешируемые элементы
test = {1, 4, "fff", (4,)}
print(type(test))

numbers.add(55)
print(numbers)
numbers.remove(2)
# umbers.remove(4444444) KeyError: 4444444
print(numbers)
