# Пример декоратора без args, kwargs

def prefix_decorator_name(func):
    def wrapper(name, surname):
        print("Prefix!",end="  ")
        result = func(name,surname)
        print("Prefix end",end="  ")
        return result
    return wrapper

def decorator_name(func):
    def wrapper(name, surname):
        result = func(name, surname)
        print("Bye bye",end="  ")
        return result
    return wrapper


@prefix_decorator_name
@decorator_name
def full_name(name, surname):
    print(f"|Hello {name} {surname}|",end="  ")

full_name("Ivan", "Petrovich") # Prefix!  |Hello Ivan Petrovich|  Bye bye  Prefix end
