class Foo:  # class Foo(object):
    def __new__(cls, *args):
        print("Method __new__")
        print(args)
        instance = super(Foo, cls).__new__(cls)
        return instance

    def __init__(self, value):
        print("Method __init__")
        self.value = value


class Baz(Foo):
    def __init__(self, value):
        super(Foo, self).__init__(value)


baz = Baz(10)  # Method __new__  (10,)  Method __init__
foo = Baz(20)  # Method __new__  (20,)  Method __init__

print(baz.value, foo.value)  # 10 20
# <__main__.Baz object at 0x000002A4708A0F10> <__main__.Baz object at 0x000002A4708A1010>
print(baz, foo)
