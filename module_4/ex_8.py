# словари
empty_dict = {}
empty_dict_1 = dict()

temp = {
    "name": "Ivan",
    "age": 33,
    "city": "Ivano-Frankovsk",
    "data": ["temp", "new"],
    "dict": {"new": "abc"},
    3: 55,
    (1,): "try"
}

temp["city"] = "Odessa"
temp["city322"] = "Kiev"
print(temp)


new = {"key": "value"}
temp.update(new)
print("aaaa", temp)

del temp["dict"]
# del temp["dict"] на 2 раз будет ошибка т.к. такого обьекта нет
print(temp)

# temp.clear() очистит словарь полностью
print(temp)

print("name" in temp)  # True
