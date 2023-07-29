from functools import reduce

numbers = [5, 6, 7]

# 1 шаг x = 0 y = 5 res = 5 # 2 шаг x = 5 y = 6 res = 11 # 3 шаг x = 11 y = 7 res = 18
sum_nums = reduce(lambda x, y: x + y, numbers, 0)
print(sum_nums)  # 18

# 1 шаг x = 1 y = 5 res = 5 # 2 шаг x = 5 y = 6 res = 30 # 3 шаг x = 30 y = 7 res = 210
mult_nums = reduce(lambda x, y: x * y, numbers, 1)
print(mult_nums)  # 210

greeting = reduce(lambda calc, nex: calc + nex, ["h", "e", "l", "l", "o"], "")
print(greeting)  # hello
