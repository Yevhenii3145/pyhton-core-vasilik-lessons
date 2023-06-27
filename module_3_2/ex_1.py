lst = ["1", "2", "3"]


def lst_func(a, b):
    lst = [a, b, "c"]
    return lst


a = lst_func("5", 6)
print(a)  # ['5', 6, 'c']
print(lst)  # ['1', '2', '3']
