class Parent:
    def custom_method(self, value, *args, **kwargs):
        print("Parent method was called")
        print(f"Value equal: {value}")
        print(f"args equal: {args}")
        print(f"kwargs equal: {kwargs}")
        print("-" * 10)


class Child(Parent):
    def custom_method(self, value, *args, **kwargs):
        super().custom_method(value, *args, **kwargs)  # Вызов родительского метода
        print("Child method was called")
        print(f"Value equal: {value}")
        print(f"args equal: {args}")
        print(f"kwargs equal: {kwargs}")
        print("-" * 10)


child = Child()
child.custom_method(5, "test", 4, name="Ivan")
# Parent method was called
# Value equal: 5
# args equal: ('test', 4)
# kwargs equal: {'name': 'Ivan'}
# ----------
# Child method was called
# Value equal: 5
# args equal: ('test', 4)
# kwargs equal: {'name': 'Ivan'}
# ----------
