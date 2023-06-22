print(1 == 2)  # False
print(1 != 2)  # True
print(1 < 2)  # True
print(1 > 2)  # False
print(1 >= 2)  # False
print(1 <= 2)  # True

a = 10
print(a == 5)  # False
print(a == 10)  # True

print("aa" == "aa")  # True
print("Paris" == "Rome")  # False
print(16 == 16.0)  # True
print(15 == "15")  # False
# print(15 > "15") #TypeError: '>' not supported between instances of 'int' and 'str'

# and, or, not
# and => *
# or => +
# not => !

print((5 < 10) and (3 < 4))  # True
print((5 < 10) and (35 < 4))  # False

print((5 < 10) or (3 < 4))  # True
print((5 < 10) or (35 < 4))  # True

a = 2 + 2 == 4 and not 2 + 2 == 6 and 3 * 3 == 2 + 2 + 2
print(a)  # False
