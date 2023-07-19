"""
LIFO (англ. last in, first out, "последним пришёл - первым вышел") - способ организации
данных или другими словами Стек (Stack). В структурированном линейном списке, организованном
по принципу LIFO,элементы могут добавляться и выбираться с одного конца, называемого
"вершиной списка".
"""

from collections import deque

MAX_LEN = 10
lifo = deque(maxlen=MAX_LEN)


def push(element):
    lifo.appendleft(element)


def pop():
    return lifo.popleft()


push("Vladymyr")
push("Ivan")
push("Petr")
push("Iryna")
print(lifo)  # deque(['Iryna', 'Petr', 'Ivan', 'Vladymyr'], maxlen=10)

name = pop()
print(name)  # Iryna
print(lifo)  # deque(['Petr', 'Ivan', 'Vladymyr'], maxlen=10)
