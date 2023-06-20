# простые типы данных
a = float(15)
print(a)  # 15.0
b = int(a)
print(b)  # 15
b = int(14.7)
print(b)  # 14
s = "4"
v = int(s)
print(v)  # 4
# строки с числами с плавающей точкой  нельзя перевести в int
# b = int("5.6")  # ValueError: invalid literal for int() with base 10: '5.6'
b = int(float("5.6"))  # а так норм
print(b)  # 5
# h = int("fdfdfddf")  # ValueError: invalid literal for int() with base 10: '5.6'
# приведение в восьмиричную систему исчисления
print(int("100", 8))  # 64
# перевод в двоичную систему исчисления
print(int("1011", 2))  # 11
# перевод в шестнадцатиричную систему исчисления
print(int("f", 16))  # 15
print(int("100", 5))  # 25
print(4.47e+8)  # 447000000.0    равносильно 4.47 * 10 **8
# чтобы взять модуль числа есть abs
print(abs(-34))  # 34
print(abs(-34.56))  # 34.56
print(pow(5, 2))  # 25
print(pow(-4.5, 2))  # 20.25
print(round(10.6))  # 11

print(round(2.665, 2))  # 2.67
print(round(2.675, 2))  # 2.67
# обьяснение почему он так окургляет:
print("{:.30}".format(2.665))  # 2.66500000000000003552713678801
print("{:.30}".format(2.675))  # 2.67499999999999982236431605997
print(0.1 + 0.3)  # 0.4
print(0.1 + 0.2)  # 0.30000000000000004
print("{:.30}".format(0.1 + 0.2))  # 0.300000000000000044408920985006
# функция print()
string = "New\tLine"
print(string)  # New     Line
new_string = "New\\tLine"
print(new_string)  # New\tLine
a, b, c, d = 1, 2, 3, 4
print(a, b, c, d, sep="*$&*__")  # 1*$&*__2*$&*__3*$&*__4
separator = "__gg__"
print(a, b, c, d, sep=separator)  # 1__gg__2__gg__3__gg__4
print(a, b, c, d, end="\n")
y = 2.5 + 3j
print(y)  # (2.5+3j)
print(type(y))  # <class 'complex'>
a = 5
b = "5"
# print(a+b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
a = "test"
b = 5
print(a + str(b))  # test5
a = "Hello world"
print(len(a))  # 11
# print("aaa"-"bbb") # TypeError: unsupported operand type(s) for -: 'str' and 'str'
print("d" * 5)  # ddddd
start = "Hi" * 5 + "\t"
second = "Niht" * 2 + "ffff"
print(start, second)  # HiHiHiHiHi       NihtNihtffff
size = 1
print(size < 0)  # False
print(size > 0)  # True
print(int(True), int(False))  # 1 0
print(float(True), float(False))  # 1.0 0.0
print(bool(1), bool(0.0))  # True False
print(bool(" "), bool(""))  # True False
print(bool(None))  # False
print(bool([]), bool(()), bool({}), bool(""))  # False False False False
print(type(None))  # <class 'NoneType'>
print(2 != 1)  # True
print(2 != 2)  # False
print(2 >= 2)  # True
print(2 > 2)  # False
print(257 is 257)  # True
