a = int(input("enter a number: "))
b = int(input("enter a number: "))

if a < b:
    temp = a
    a = (a + b) / 2
    b = temp * b
else:
    temp = b
    b = (b + a) / 2
    a = temp * a
print("a", a, "b", b)

a = int(input("enter a number: "))
b = int(input("enter a number: "))

if a < b:
    a, b = (a + b) / 2, a * b
else:
    b, a = (b + a) / 2, b * a
print("seond try ", "a", a, "b", b)

a = int(input("enter a number: "))
b = int(input("enter a number: "))

a, b = ((a + b) / 2, a * b) if a < b else (a * b, (a + b) / 2)
print("third try ", "a", a, "b", b)
