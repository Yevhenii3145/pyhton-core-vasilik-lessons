import random

l = list(range(1, 37))
print(l) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
random.shuffle(l)
print(l) # [26, 19, 7, 14, 22, 3, 11, 10, 25, 35, 5, 33, 12, 21, 31, 8, 9, 27, 6, 23, 1, 16, 28, 34, 32, 15, 4, 29, 13, 24, 30, 18, 2, 20, 36, 17]

print(random.choice(l)) # 7 выберет один случайный элемент из последовательнсти l
print(random.sample(l, k=3)) # [8, 36, 16] выберет три случайных элемента из последовательнсти l
# print(random.sample(l, k=88)) # ValueError: Sample larger than population or is negative
