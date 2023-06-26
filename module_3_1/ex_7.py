def total(a = 5, *args, **phone_book):
    print("a", a)
    # проход по всех элементах кортежа
    for single_item in args:
        print("single_item", single_item)

    #проход по всех элементах словаря
    for key,value in phone_book.items():
        print(key, value)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
