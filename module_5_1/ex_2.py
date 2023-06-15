"""
Поиск в строке
"""

s = "Hello world"

start = 0
end = 7


# 1 индекс первого вхождения
print(s.find("el", start, end))
# -1 если не нашло
print(s.find("d", start, end))

s = "Hello world"

print(s.rfind("o"))  # 7 индекс первого вхождения справа
