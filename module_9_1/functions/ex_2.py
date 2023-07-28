# функция как обект первого класса
# Второе требование - функция может быть передана в другую функцию как аргумент

def mul(a, b):
    return a * b


def add(a, b):
    return a + b


def ops(a, b, func):  # func - передаём функцию как параметр
    return func(a, b)


result_mul = ops(2, 4, mul)
print(result_mul)  # 8


result_add = ops(2, 4, add)
print(result_add)  # 6
