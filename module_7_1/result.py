# import calc

# print(calc.add(2, 2))  # 4
# print(calc.substract(3, 1))  # 2


# from calc import add

# print("From add result =", add(3,3)) #From add result = 6
# #print("From substract result =", substract(4,1)) # NameError: name 'substract' is not defined


# from calc import *

# print("From add result = ", add(3,3))
# print("From substract result = ", substract(3,2))

# import math  # импорт всей библиотеки
# from math import sqrt, factorial

# print(sqrt(16)) # 4.0
# print(factorial(6)) #720

# import sys
# print(sys.path) # ['c:\\Users\\Admin\\Desktop\\python-core-vasilik-lessons\\module_7_1', 'C:\\Python311\\python311.zip',...]

import datetime
from datetime import date as d
import time

print(time.time()) #1689100560.332242 # время от 1.01.1970 в секундах

print(d.fromtimestamp(454554)) # 1970-01-06

# выдаст всё, что есть в файле
print(dir(datetime)) # ['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
