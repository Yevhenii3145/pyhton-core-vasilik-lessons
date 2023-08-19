# Декораторы классов
def class_decorator(cls):
    print("---Decorator class---")
    # new_cls = cls
    # new_cls.value = 55
    cls.value = 55
    # cls.description = "Core 16 Module 11 Lesson 2"
    return cls


def class_decorator_2(cls):
    print("---Decorator class 2---")
    cls.description = "Core 16 Module 11 Lesson 2"
    return cls


def method_decorator(func):
    def wrapper(self, *args):
        print("---Decorator run---")
        result = func(self, *args)
        print("---Decorator end---")
        return result
    return wrapper


@class_decorator
@class_decorator_2
class TestClass:
    name = "TestClass"

    @method_decorator
    def info(self, user):
        return f"Hello {user}. This is {self.name}"


t = TestClass()
print(t.info("Ivan"))
"""
---Decorator class 2---
---Decorator class---
---Decorator run---
---Decorator end---
Hello Ivan. This is TestClass
"""

print(t.value)  # 55
t.value = 22
print(t.value)  # 22
print(t.description)  # Core 16 Module 11 Lesson 2
t.description = "Core 16 Module 11 Lesson 2. It's amazing!"
print(t.description)  # Core 16 Module 11 Lesson 2. It's amazing!
