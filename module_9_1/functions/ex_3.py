# функция как обькт первого класса
# Третье требование - функция может быть возвращена из функции как результат

def mul(a, b):
    return a * b


def add(a, b):
    return a + b

def ops(operator: str):
    if operator == "*":
        return mul
    elif operator == "+":
        return add
    else:
        raise ValueError("Operator not supported")


try:
    f_mul = ops("*")
    print(f_mul) # <function mul at 0x0000025B8EC5D120>
    result = f_mul(2,10)
    print(result) # 20
except ValueError:
    print("Operator '*' failed")

try:
    f_add = ops("+")
    print(f_add) # <function add at 0x00000296BCD8CF40>
    result = f_add(2,10)
    print(result) # 12
except ValueError:
    print("Operator '+' failed")

try:
    f_div = ops("/")
    print(f_div)
    result = f_div(2,10)
    print(result) # 12
except ValueError:
    print("Operator '/' failed") # Operator '/' failed
