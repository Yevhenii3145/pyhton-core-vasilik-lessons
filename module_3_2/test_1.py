def hello(text):
    print(f"hello -> {text}")
    # return None


print("The name is: {0}".format(__name__)) # The name is: __main__

if __name__ == "__main__":  # если мы открываем этот код в другом файле то всё, что ниже не выполнится
    print("First line before call func")

    hello("call func")

    print("Second line after call func")
