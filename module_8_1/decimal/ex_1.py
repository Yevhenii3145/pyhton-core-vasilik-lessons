"""
Необходимость использования. Настройка точности
"""

from decimal import Decimal, getcontext

f = 0.2 + 0.1 + 0.3 - 0.5
print(f) # 0.10000000000000009

rf = Decimal("0.2") + Decimal("0.1") + Decimal("0.3") - Decimal("0.5")
print(rf) # 0.1
print(type(rf)) # <class 'decimal.Decimal'>

not_precision = Decimal("1") / Decimal("3")
print(not_precision) # 0.3333333333333333333333333333

getcontext().prec = 6 # Атрибут который управляет точностью расчётов
precision = Decimal("1") / Decimal("3")
print(precision) # 0.333333
precision = Decimal("11") / Decimal("3")
print(precision) # 3.66667
precision = Decimal("44") / Decimal("3")
print(precision) # 14.6667
