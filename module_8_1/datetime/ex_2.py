from datetime import datetime

# Перевод строки в дату и назад
td = "01.11.2022"
d = datetime.strptime(td, "%d.%m.%Y")
print(d) # 2022-11-01 00:00:00
print(type(d)) # <class 'datetime.datetime'>
print(d.date()) # 2022-11-01
print(d.time()) # 00:00:00

print(d.year, d.month, d.minute) # 2022 11 0

other_d = d.replace(month=5, day=12, hour=15, minute=55)
print(other_d) # 2022-05-12 15:55:00
str_d = other_d.strftime("%Y/%d/%m %H:%M:%S")
print(str_d) # 2022/12/05 15:55:00

a = datetime.now()

print(a.strftime("%Y, %B %e")) # 2023, July 17
print(a.strftime("%d %h %Y")) # 17 Jul 2023
