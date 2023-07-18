"""
Порівняння двох десяткових чисел
Значення 0 вказує, що обидва числа дорівнюють,
значення 1 вказує, що перше число більше за друге число,
а значення -1 вказує, що перше число менше за друге.
"""

from decimal import Decimal

print(Decimal("1.2").compare(Decimal("1.1"))) # 1
print(Decimal("1.2").compare(Decimal("1.7"))) # -1
print(Decimal("1.2").compare(Decimal("1.2"))) # 0

print(0.1 + 0.2 == 0.3) # False

num1 = Decimal("0.1") + Decimal("0.2")
num2 = Decimal("0.3")
print(num1 == num2) # True
print(type(num1)) # <class 'decimal.Decimal'>
print(num1.compare(num2)) # 0

print(Decimal(0.1) + Decimal(0.2) == Decimal(0.3)) # Fals т.к. это не строки
print(Decimal(0.1) + Decimal(0.2)) # 0.3000000000000000166533453694
print(Decimal(0.3)) # 0.299999999999999988897769753748434595763683319091796875
print(Decimal("0.3")) # 0.3
