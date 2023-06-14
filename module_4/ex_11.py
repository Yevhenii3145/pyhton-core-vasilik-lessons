temp = {
    "name": "Ivan",
    "age": 33,
    "city": "Ivano-Frankovsk",
    "data": ["temp", "new"],
    "dict": {"new": "abc"},
    3: 55,
    (1,): "try"
}

# dict_keys(['name', 'age', 'city', 'data', 'dict', 3, (1,)])
print(temp.keys())
print(list(temp.keys()))  # конвертируем в список
print(list(temp.values()))
print(temp.items())  # dict_items([('name', 'Ivan'), ('age', 33),.....])
