try:
    value_1 = input("Please set value_1: ")
    value_2 = input("Please set value_2: ")
    res = int(value_1) / int(value_2)
except (ZeroDivisionError, ValueError):
    print("You can't devide by zero")
except Exception as e:  # если не знаем какая может быть ошибка
    # New mistake: invalid literal for int() with base 10: 'r'
    print(f"New mistake: {e}")
else:
    print(f"Result is: {res}")
finally:  # выполнится в любом случае
    print("Happy end")
