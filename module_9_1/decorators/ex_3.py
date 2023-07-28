# сделать декоратор, который возвращает кортеж с результатом функции подсчета факториала и временем её выполнения

from time import time, sleep


def time_counter(func):
    def interval(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        diff = time() - start
        return result, diff
    return interval


@time_counter
def test_func(a, b):
    sleep(b)
    return a + b


print(test_func(3, 5))  # (8, 5.000865459442139)
print(test_func(4, 2))  # (6, 2.0003368854522705)
