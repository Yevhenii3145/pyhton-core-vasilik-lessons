"""
FIFO (англ. first in, first out - "первым пришёл - первым вышел") - способ организации
данных или другими словами
Это выражение описывает принцип технической оброботки очереди или обслуживания конфликтных
требований путём упорядовачивания процесса по принципу: "первым пришёл - первым обслуженный".
Тот кто приходит первым, тот и обслуживается первым, кто придёт следующим, ждёт пока
обслуживание первого не будет оконченно, и так далее.
"""

from collections import deque

MAX_LEN = 10
fifo = deque(maxlen=MAX_LEN)


def push(element):
    fifo.append(element)


def pop():
    return fifo.popleft()


push("Vladymyr")
push("Ivan")
push("Petr")
push("Iryna")
print(fifo)  # deque(['Vladymyr', 'Ivan', 'Petr', 'Iryna'], maxlen=10)
name = pop()
print(name)  # Vladymyr
print(fifo)  # deque(['Ivan', 'Petr', 'Iryna'], maxlen=10)
a = list(fifo)
print(a)  # ['Ivan', 'Petr', 'Iryna']
