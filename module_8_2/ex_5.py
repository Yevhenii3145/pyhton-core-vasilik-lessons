# Написать функцию, которая определяет какой день недели у определённой даты в виде "день-месяц-год"

from datetime import datetime
import calendar

# Проверим, высокосный ли год
print(calendar.isleap(2020))  # True

days_name = {
    0: "понедельник",
    1: "вторник",
    2: "среда",
    3: "четверг",
    4: "пятница",
    5: "суббота",
    6: "воскресенье",
}


def day_of_week(date: str):
    d, m, y = date.split("-")
    date = datetime(day=int(d), month=int(m), year=int(y))
    d_name = days_name.get(date.weekday())
    return d_name


print(day_of_week("31-01-2005"))  # понедельник
print(day_of_week("25-05-1990"))  # пятница
print(day_of_week("10-12-1988"))  # суббота
print(day_of_week("03-11-2022"))  # четверг
