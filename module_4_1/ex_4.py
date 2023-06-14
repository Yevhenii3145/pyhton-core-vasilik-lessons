# добавление списков
our_list = ["new", "new_1", "new_2", "new_3", "new_4"]

# append мутирует исходный массив
our_list.append("ffffff")
print(our_list)

# 2-индекс 33-сам элемент который вставляем
our_list.insert(2, 33)
print(our_list)

new_l = ["rrr", "bbb"]
our_list.append(new_l)  # добавит массив new_1 в our_list
print(our_list)
# extend сольет два массива в 1
our_list.extend(new_l)  # мутирует исходный массив
print(our_list)
# our_list.extend(123) TypeError: 'int' object is not iterable
our_list += new_l

# проитерирется по строке и добавит отдельно каждый элемент
our_list.extend("123")
print(our_list)

our_list = ["new", "new_1", "new_2", "new_3", "new_4"]
del our_list[2]  # удаление по индексу
print("aaaa", our_list)

temp = our_list.remove("new_4")  # None
print(temp)
print(our_list)

# по дефолту удалит последний элемент
test = our_list.pop(1)  # new_1
print(test)
print(our_list)

our_list = ["new", "new_1", "rrr", "new_2", "new_3", "new_4", "rrr"]

# remove находит самое первое вхождение элемента и удаляет его
our_list.remove("rrr")
print(our_list)

# del our_list - удалит сразу весь список вместе с ячейкой памяти
