"""
Метод: isdigit
----
Данный список, каждым элементом которого является строка  символов, которые состаят из одних цифр.
Упорядочить элементы массива по возростанию из числовых значений и вывести на экран.
От максимального элемента отнять значение минимального и вывести разницу на экран.
Подсчитать среднее значение всех элементов.
"""

numbers = ["123", "456", "321", "10", "75", "abc", "23c"]


def senitize(data):
    result = []
    for el in data:
        if el.isdigit():
            result.append(el)
    return result


def transform_to_int(data):
    result = []
    for el in data:
        result.append(int(el))
    return result


san_nums = senitize(numbers)
san_nums = transform_to_int(san_nums)
san_nums.sort()
print(san_nums)  # [10, 75, 123, 321, 456]

print(max(san_nums) - min(san_nums))  # 446
print(sum(san_nums) / len(san_nums))  # 197.0
