# Карринг - это преобразование функции от множества аргументов на набор функций,
# каждая из которых является функцией от одного аргумента.Мы можем передать часть аргументов
# в функцию и получить назад функцию,которая ждёт другие аргументы.

# У нас есть функция, которая принимает 2 параметра name, msg и с помощью карринга мы разбиваем на несколько ф-ций
# с одним параметром (код ниже) def greeting(name)

def greeting_simple(name, msg, value):
    return f"{name} - {msg}: {value}"

print(greeting_simple("Ivan", "Go to work!","55"))
print(greeting_simple("Ivan", "Go to home!","55"))


def greeting(name): # внешняя ф-я
    def message(msg): # внутренняя ф-я
        def inner_second(value):
            return f"{name} - {msg}: {value}"
        return inner_second
    return message


msg_for_oksana = greeting("Oksana") # внутрення ф-я будет иметь доступ к name из-за замыкания
total_msg = msg_for_oksana("Go to work!")
print(total_msg("55")) # Oksana - Go to work!: 55
