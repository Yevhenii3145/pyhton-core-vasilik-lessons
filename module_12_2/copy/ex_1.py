"""
Интерпретатор Python ленивый и если его явно не попросить создать копию объекта,
он создаст новую ссылку на тот же объект. Не всегда такое поведение приветствуется.
Для создания копии объекта в пакете copy есть функции:
-copy - поверхностная копия
-deepcopy - глубокая копия
"""
from copy import copy, deepcopy

l = [1, 2, 3, ["a", "b", "c", 5]]

test_l = l[:]
l_copy = copy(l)
l_deep = deepcopy(l)

print(test_l == l_copy, l_copy == l_deep, test_l == l_deep)  # True True True
print(test_l is l_copy, l_copy is l_deep,
      test_l is l_deep)  # False False False

l[0] = 9
# [9, 2, 3, ['a', 'b', 'c', 5]] [1, 2, 3, ['a', 'b', 'c', 5]] [1, 2, 3, ['a', 'b', 'c', 5]] [1, 2, 3, ['a', 'b', 'c', 5]]
print(l, test_l, l_copy, l_deep)
l[3][3] = '3'
# [9, 2, 3, ['a', 'b', 'c', '3']] [1, 2, 3, ['a', 'b', 'c', '3']] [1, 2, 3, ['a', 'b', 'c', '3']] [1, 2, 3, ['a', 'b', 'c', 5]]
print(l, test_l, l_copy, l_deep)
