temp = []
temp = list()

test = [1, 2, 3, 4, 5]
print(test)
print(type(test))

temp = ["a", "b", "c"]
print(temp)

a = temp
print(a)
print(type(a))

a[0] = 33
a[1] = str(44)
print(a)
a[2] = "lorem ipsum dolore"
print(a)
print(len(a))

a = [1, 2, 3]
c = list(a)
d = a[:]
print(f"a: {a}")
print(f"c: {c}")
print(f"d: {d}")

a = "1999"
b = list(a)
print(b)

birthday = "3/5/1993"
t = birthday.split(".")
s = birthday.split("/")
print(t)
print(s)

r = "a|b|c|d|e|f|||g"
q = r.split("|")  # команда split не изменяет исховный массив поэтому нужно присвоить к переменной
print(q)

y = ["Python", "is", "the", "best", "language"]
e = " ".join(y)
print(e)
