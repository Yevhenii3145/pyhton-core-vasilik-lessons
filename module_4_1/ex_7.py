# кортежи
e_tuple = ()
print(e_tuple)
print(type(e_tuple))

a = "test",
b = "test", "new", "tmp", "code"
print(a)
print(type(a))
print(type(b))

# присвоение элементов кортежа к переменным, если єлемента 4 то и переменных нужно 4
a_1, a_2, a_3, a_4 = b
print(a_1)
print(a_2)
print(a_4)
print(type(a_1))  # str

a_1, a_2, *_ = b
print(a_1)
print(a_2)
print(_)

*tt, a_2 = b
print(a_2)
print(tt)

a = [1, 4, 6]
b = tuple(a)
print(b)
