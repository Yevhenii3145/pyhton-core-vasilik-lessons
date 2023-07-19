"""
Реализовать функцию, которая возвращает n чисел, которые чаще всего встречаюся
и n наименее часто встречающихся, из файла
"""

from collections import Counter

filename = 'numbers.txt'

numbers_list = []
with open("numbers.txt", "r") as file:
    for line in file:
        line = line.replace("\n", "")
        nums = line.split(",")
        numbers_list.extend(nums)


def my_counter(some_list: list, n: int) -> tuple:
    numbers_counter = Counter(some_list)

    if n > len(numbers_counter):
        print(f"Your second arg {n} must be less then len of list")
        return
    most_common = numbers_counter.most_common(n)
    print("MOST COMMON", most_common, end="  ")
    print("ALL LEN", len(numbers_counter), end="  ")
    all_most_common = numbers_counter.most_common(len(numbers_counter))

    revers_of_all_m_c = all_most_common[::-1]
    less_common = revers_of_all_m_c[: n]
    print("LESS COMMON", less_common)

    return (most_common, less_common)


# MOST COMMON [('65', 128), ('8', 123)]  ALL LEN 100  LESS COMMON [('84', 75), ('28', 80)]
my_counter(numbers_list, 2)
# Your second arg 105 must be less then len of list
my_counter(numbers_list, 105)

new_list = [1, 5, 6, 8, 9, 12, 1, 4, 5, 12, 10, 99, 55, 36, 58, 1, 9, 5, 34]
# MOST COMMON [(1, 3), (5, 3), (9, 2)]  ALL LEN 13  LESS COMMON [(34, 1), (58, 1), (36, 1)]
my_counter(new_list, 3)
