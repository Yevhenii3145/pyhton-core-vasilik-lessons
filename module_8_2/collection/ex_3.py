"""
defaultdict
colletions.defaultdict ничем не отличается от обычного словаря
за исключением того, что по умоланию всегда вызывается функция,
которая возвращает значение
"""
from collections import defaultdict

data_d = defaultdict(list)

data_d[0].append(11)
data_d[0].append(1)
data_d[0].append(100)
print(data_d)  # classic = {0: [11, 1, 100]}

colors = [("yellow", 1), ("blue", 3), ("yellow", 5), ("blue", 10), ("red", 12)]
colors_d = defaultdict(list)

for key, value in colors:
    colors_d[key].append(value)
# defaultdict(<class 'list'>, {'yellow': [1, 5], 'blue': [3, 10], 'red': [12]})
print(colors_d)
