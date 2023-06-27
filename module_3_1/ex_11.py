def outer():
    x = "локальная переменная"

    def inner():
        nonlocal x
        # изменяе x из уровнем выше
        x = "нелокальная переменная x"
        # внутренняя функция:  нелокальная переменная x
        print("внутренняя функция: ", x)

    inner()
    # внешняя функция:  нелокальная переменная x
    print("внешняя функция: ", x)


outer()
