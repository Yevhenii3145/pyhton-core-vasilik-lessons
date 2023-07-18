"""
Класс datetime.timedelta - разница между двумя моментами времени, с точностью до микросекунд.
"""

from datetime import datetime, timedelta

d = datetime.now()

interval = timedelta(days=4)
print(interval, type(interval)) # 4 days, 0:00:00 <class 'datetime.timedelta'>
finish_date = d + interval
print(finish_date) # 2023-07-21 12:35:06.895961

birth_date = datetime(1993, 2, 27)
spent = datetime.now() - birth_date
print("spent", spent) # spent 11097 days, 12:40:54.557977
