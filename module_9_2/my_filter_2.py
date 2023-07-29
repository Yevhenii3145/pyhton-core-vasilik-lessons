nums = [i for i in range(1, 10)]
print(nums)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

sq = map(lambda x: x ** 2, nums)
result = filter(lambda value: bool(value % 2), sq)
print(list(result))  # [1, 9, 25, 49, 81]

sq = map(lambda x: x ** 2, nums)
result = filter(lambda value: not bool(value % 2), sq)
print(list(result))  # [4, 16, 36, 64]


result = filter(lambda value: bool(value % 2), map(
    lambda x: x ** 2, [i for i in range(1, 10)]))
print(list(result))  # [1, 9, 25, 49, 81]

result = map(lambda x: x ** 2, filter(lambda value: bool(value %
             2), [i for i in range(1, 10)]))
print(list(result))  # [1, 9, 25, 49, 81]
