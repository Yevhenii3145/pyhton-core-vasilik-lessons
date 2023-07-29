"""
Напишите decorator, который записывает в консоль два сообщения журнала:
: call [порядковый номер вызова функции]: [имя функции][её аргументы]\n
: result: [имя функции][результат]\n
"""
import sys


def logger(func):
    call_count = 0

    def inner(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        sys.stdout.write(f"call [{call_count}]: [{func.__name__}][{args}] |\n")
        result = func(*args, **kwargs)
        sys.stdout.write(f" result: [{func.__name__}][{result}]\n")
        return result
    return inner


@logger
def add(x, y):
    return x + y


@logger
def mul(x, y):
    return x * y


print(add(3, 5))  # call [1]: [add][(3, 5)] | result: [add][8] 8
print(mul(3, 5))  # call [1]: [mul][(3, 5)] | result: [mul][15] 15
print(add(4, 10))  # call [2]: [add][(4, 10)] | result: [add][14] 14
print(mul(4, 10))  # call [2]: [mul][(4, 10)] | result: [mul][40] 40
print(add(5, 5))  # call [3]: [add][(5, 5)] | result: [add][10] 10
print(mul(5, 5))  # call [3]: [mul][(5, 5)] | result: [mul][25] 25
