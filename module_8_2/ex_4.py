"""
Напишите функцию, которая принимает на вход три целых числа: день, месяц и год. Функция
должна возвращать порядковый номер заданного дня в указанном году.

Результат функции: номер года и порядковый номер дня в указанном году - оба в целостном
формате.
"""

from datetime import datetime, date


def transfer_to_ordinal_date(day: int, month: int, year: int) -> tuple:
    d = date(year, month, day).toordinal()
    # +1, чтобы скомпенсировать отнятый день
    diff = d - date(year, 1, 1).toordinal() + 1
    return year, int(diff)


print(transfer_to_ordinal_date(18, 1, 2023))  # (2023, 18)
print(transfer_to_ordinal_date(31, 12, 2023))  # (2023, 365)
print(transfer_to_ordinal_date(18, 7, 2023))  # (2023, 199)


"""
Разработайте функцию, которая принимает як единственный параметр порядковую дату, которая включает в себя год и день
по порядку. Как результат функция должна возвращать день и месяц, которые соответствуют переданной порядковой дате.
"""


def transfer_to_date(ordinal: int, year: int):
    d_temp = date(year, 1, 1).toordinal()
    d = datetime.fromordinal(d_temp - 1 + ordinal)
    return d


print(transfer_to_date(99, 2001))  # 2001-04-09 00:00:00
print(transfer_to_date(365, 2023))  # 2023-12-31 00:00:00

current = datetime.now().toordinal()
print(current)  # 738719  кол-во дней с 01.01.01
