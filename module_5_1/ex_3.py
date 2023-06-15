"""
Метод: find
----
Дано строка символов.
Исключить из этой строки группы символов между скобками [,].
Сами скобки тоже должны быть исключены.
Предполагается,что в каждой паре скобок нет других скобок.
"""

string = "Виключаючи із цієї [рядки групи] символів, [розташовані між] дужками [,]."

# start_index = string.find("[")
# end_index = string.find("]")

# new_str = string[:start_index] + string[end_index + 1:]
# print(new_str)

def sanitize(string):
    new_string = string[:]
    while True:
        start_index  = new_string.find("[")
        end_index = new_string.find("]")
        if start_index == -1:
            break
        new_string = new_string[:start_index] + new_string[end_index + 1:]
    return new_string

print(sanitize(string))
