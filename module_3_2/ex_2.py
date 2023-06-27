def sum(first: int, *args) -> int:
    sum = first
    for element in args:
        sum = sum + element
    return sum


result = sum(3, 2, 5, 8, 10)
print(result)  # 28
