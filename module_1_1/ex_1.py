a = 10
b = 10
V = 10
_c = 10
__u = 88  # по договоренности __ означает, что переменная приватна, её не нужно изменять
#!f = 10 # не правильно
# ^h = 10  не может начинаться со спец символов
# 1h = 10 # не может начинаться с цифры
h1 = 10
number_value = 5
numberValue = 5  # camelCase не используют в пайтон
number_value_temp_1 = 5
number_value_SDK = 5
PI = 3.14  # константа
привет = 5  # кирилица не принята
# нельзя использовать зарезирвированые слова
# True,False,and,as class,for,if,is,while
a = 4 + 6
a = 5 / 3
print(a)  # 1.6666666666666667
a = 5 // 3
print(a)  # 1 целочисленное деление
a = 8 % 3
print(a)  # 2 отаток от деления
result_pow = 3 ** 2
print(result_pow)  # 9
# если степень или само число дробное чило то и результат  будет дробным
result_pow = 3 ** 2.0
print(result_pow)  # 9.0
result_pow = 3.0 ** 2
print(result_pow)  # 9.0
result = 4 / 2  # всегда при делении будет дробное число
print(result)  # 2.0
# print(05 + 5) # SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
# print(6/0)  # ZeroDivisionError: division by zero
b = 45
c = 30
print(c - b)  # -15
print(c - 5)  # 25
f = 55
f = f - 4
print(f)  # 51
h = 22
h -= 2
print(h)  # 20
k = 10
k /= 5
print(k)  # 2.0
a = 8
b = 1
a, b = b, a
print(f"a: {a} b: {b}")  # a: 1 b: 8
d = 4
print(type(d))  # <class 'int'>
n = 4.4
print(type(n))  # <class 'float'>
t = 'don\'t'  # используем экранирование,чтобы указать, что это не конец троки
print(t)
str = "Hello"
str += " world!"
print(str)  # Hello world!
a = "Hello"
b = "world!"
new_str = f"{a} {b}"
# f строки работают намного быстрее
print(new_str)  # Hello world!
a = "test"
print(id(a))  # 2857798171888
a += " "  # сама строка не изменяется, теперь а ссылается на другую строку
print(id(a))  # 2354310644528
b = 3333.4444
c = 3333.4444
print(id(b))  # 1553477975408
# хоть числа одинаковые,а ссылки разные
print(id(c))  # 2574623751568
b = 256
c = 256
print(id(b))  # 140705743500040
# здесь уже они ссылаются на одну ячейку
print(id(c))  # 140705743500040
t = "skra"
v = "skra"
print(id(t))  # 2277050449328
# идентичное id т.к. одна и та же строка, а строка -неизменный тип данных
print(id(v))  # 2324287815088
a = input("Please enter some value:")  # 179
print(f"YOUR INPUT IS: {a}")  # YOUR INPUT IS: 179
