"""
collection.deque(iterable, [maxlen]) - создаёт очередь из объекта, который
итерируется, с максимальной длиной
Очереди очень похожи на списки, за исключением того, что добавлять и удалять
элементы можно или справа, или слева.
Методы определённые в deque:
append(x) - добавляет x к концу.
appendleft(x) - добавляет x в начало.
clear() - очищает очередь.
count(x) - количество элементов, равных x.
extend(iterable) - добавляет в конец все элементы iterable.
extenleft(iterable) - добавляет сначала все элементы iterable (начиная с последнего
элемента iterable).
pop() - удаляет и возвращает последний элемент очереди.
popleft() - удаляет и возвращает первый элемент очереди.
remove(value) - удаляет первое вхождение value.
reverse() - разворачивает очередь.
rotate(n) - полностью переносит n элементов из конца на начало (если n отрицательное,
то наоборот).
"""

from collections import deque

l = list(range(1, 10))
l_deque = deque(l)
print(l_deque)  # deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(deque(l, 5))  # deque([5, 6, 7, 8, 9], maxlen=5)
l_deque.appendleft(10)
print(l_deque)  # deque([10, 1, 2, 3, 4, 5, 6, 7, 8, 9])
l_deque.append(11)
print(l_deque)  # deque([10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11])
print(l_deque.count(10))  # 1
print(l_deque.index(10))  # 0
# print(l_deque.index(135)) # ValueError: 135 is not in deque

l_deque.rotate(2)
# два последних элемента поставит в начало очереди  9 и 11
print(l_deque)  # deque([9, 11, 10, 1, 2, 3, 4, 5, 6, 7, 8])

l_deque.reverse()
# развернет всю очередь
print(l_deque)  # deque([8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 9])
