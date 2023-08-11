class Parent:
    @staticmethod
    def custom_static_method():
        print("Parent method was called")


class Child(Parent):
    @staticmethod
    def custom_static_method():
        # Вызов родительского метода
        super(Child, Child).custom_static_method()
        print("Child method was called")


child = Child()
child.custom_static_method()  # Parent method was called  Child method was called
