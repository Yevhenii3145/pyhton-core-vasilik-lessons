def print_max(a,b):
    result = None
    if a > b:
        result = a - b
    elif a == b:
        result = a * b
    elif a < b:
        result = a / b
    return result

a = 3
b = 4
result = print_max(10, b) # прямая передача значений
print(result)
