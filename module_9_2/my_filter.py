payment = [100, -5, 200, 35, -33]


def is_negative_number(number: int) -> bool:
    if number < 0:
        return True
    return False


negative_values = filter(is_negative_number, payment)
print(list(negative_values))  # [-5, -33]

negative_values = filter(lambda num: num < 0, payment)
print(list(negative_values))  # [-5, -33]

positive_values = filter(lambda num: num > 0, payment)
print(list(positive_values))  # [100, 200, 35]
