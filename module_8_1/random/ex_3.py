"""
Какое минимальное количество раз вы должны подкинуть монетку, чтобы трижды подряд выпал или орёл, или решка?
random.randint(A,B) - cлучайное целое число N, A <= N <= B
"""

import random

d = {
    1: "Орёл",
    2: "Решка"
}

count_O = 0
count_P = 0
sequence = []

while count_O < 3 and count_P < 3:
    trial = random.randint(1, 2)
    if trial == 1:
        count_O += 1
        count_P = 0
    else:
        count_O = 0
        count_P += 1
    sequence.append(d[trial])

print(f"полученно последовательность: {sequence}")

if count_O == 3:
    print("Выпало три Орла подряд")
else:
    print("Выпало три Решки подряд")
print(f"Количество попыток: {len(sequence)}")
