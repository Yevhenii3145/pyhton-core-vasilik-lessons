# функция как обьект первого класса
# Первое требование - функция может быть сохранена в переменной или структуре данных

def mul(a, b):
    return a * b


f = mul  # сохранение функции в переменной
result = f(2, 3) # вызываем функцию через переменную
print(result) # 6

field = {
    "a": 2,
    "b":3,
    "func": f
}

n = field.get("func")
print(n) # <function mul at 0x0000016FA609CF40>
result = field.get("func")(field.get("a"),11) # 22
print(result) # 6

result = field.get("func")(5,6)
print(result) # 30
