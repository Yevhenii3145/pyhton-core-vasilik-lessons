x = 50  # global


def test(x):
    print(f"x is: {x}")
    x = 33  # local
    print("x is changed to: ", x)


test(x)
print("x is still: ", x)
