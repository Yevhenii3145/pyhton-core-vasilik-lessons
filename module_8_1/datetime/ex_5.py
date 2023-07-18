# Преобразование timestamp в строку
from datetime import datetime

seconds = 1689590626.423964

date_time = datetime.fromtimestamp(seconds)
print(date_time) # 2023-07-17 13:43:46.423964
str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")
print(str_date_time) # 2023-07-17 13:43:46.423964
str_time = date_time.strftime("%I %p %M:%S")
print(str_time) # 01 PM 43:46
