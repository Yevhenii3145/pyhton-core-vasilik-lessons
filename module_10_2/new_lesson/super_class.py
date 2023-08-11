class Parent:
    @classmethod
    def custom_class_method(cls):
        print("Parent method was called")


class Child(Parent):
    @classmethod
    def custom_class_method(cls):
        super(Child, cls).custom_class_method()  # Вызов родительского метода
        print("Child method was called")


child = Child()
child.custom_class_method()  # Parent method was called Child method was called
