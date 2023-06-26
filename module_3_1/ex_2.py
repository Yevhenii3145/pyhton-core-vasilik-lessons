def is_none(value):
    if value is None:
        print("It's None")
    elif value:
        print("It's True")
    else:
        print("It's False")


is_none(None)
is_none(True)
is_none(False)
is_none(0)
is_none(0.0)
is_none("")
is_none(" ")


def fun():
    pass


print(fun())  # None
