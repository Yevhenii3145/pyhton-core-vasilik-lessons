from datetime import datetime

# Создание даты
date = datetime(year=2023,month=7,day=17)
print(date) # 2023-07-17 00:00:00
date = datetime(year=2023,month=7,day=17, hour=11,minute=31,second=38)
print(date) # 2023-07-17 11:31:38
print(type(date)) # <class 'datetime.datetime'>
print(date.date()) # 2023-07-17
print(date.time()) # 11:31:38
print(datetime.now()) # 2023-07-17 11:35:00.246171 берёт системное время, или время из сервера
print(datetime.today()) # 2023-07-17 11:36:09.702332
print(datetime.now().time()) # 11:41:13.186972
print(date.isoformat()) # 2023-07-17T11:31:38
