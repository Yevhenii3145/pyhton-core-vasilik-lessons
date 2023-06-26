x = 50  # global


def test():
    global x
    print(f"x is: {x}")
    x = 33
    print("x is changed to: ", x)


test()
print("global x changed to: ", x) # 33
