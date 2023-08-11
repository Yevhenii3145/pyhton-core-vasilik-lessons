class Parent:
    def custom_method(self):
        print("Parent method was called")


class Child(Parent):
    def custom_method(self):
        super().custom_method()  # Вызов родительского метода
        print("Child method was called")


child = Child()
child.custom_method()  # Parent method was called Child method was called
