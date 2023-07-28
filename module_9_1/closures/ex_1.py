# Замыкание

# Особенность существования вложенных локальных пространств имён и тот факт,что они создаются динамичесски,
# даёт возможность использовать механизм замыканий в Python.

def outer():
    message = "Hi there!"
    def inner():
        print(message)
    return inner

f = outer()
f() # Hi there!

def greeting(name): # внешняя ф-я
    def message(msg): # внутренняя ф-я
        return f"{name} - {msg}"
    return message

msg_for_ivan = greeting("Ivan") # внутрення ф-я будет иметь доступ к name из-за замыкания
msg_for_oksana = greeting("Oksana") # внутрення ф-я будет иметь доступ к name из-за замыкания

print(msg_for_ivan("Go to home!")) # Ivan - Go to home!
print(msg_for_ivan("Go to work!")) # Ivan - Go to work!

print(msg_for_oksana("Good job!")) # Oksana - Good job!
print(msg_for_oksana("have a nice day")) # Oksana - have a nice day
