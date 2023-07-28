# Декораторы
# шаблон проктирования, который состоит в том,чтобы расширять существующий функционал,
# не внося изменений в код этого функционала

def greeting(name):
    print(f"My name is {name}", end="  ")


def greeting_decorator(func):
    def wrapper(*args,**kwargs):
        print("Hello", end="  ")
        result = func(*args,**kwargs)
        print("Have a nice day")
        return result
    return wrapper

greeting("Ivan")
print("")

changed_greeting = greeting_decorator(greeting)
changed_greeting("Ivan") # Hello  My name is Ivan  Have a nice day
