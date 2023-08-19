# инкапсуляция
class A:
    def _protected(self):
        print("Its protected method")

    def __private(self):
        print("Its private method")


a = A()
a._protected()  # Its protected method

# a.__private() # AttributeError: 'A' object has no attribute '__private'. Did you mean: '_A__private'?

a._A__private()  # Its private method
