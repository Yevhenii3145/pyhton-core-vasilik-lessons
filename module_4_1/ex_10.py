temp = {
    "name": "Ivan",
    "age": 33,
    "city": "Ivano-Frankovsk",
    "data": ["temp", "new"],
    "dict": {"new": "abc"},
    3: 55,
    (1,): "try"
}

print(temp["name"])
# print(temp["name11111"]) KeyError: 'name11111'
print(temp.get("name"))

# None -по дефолту или нет такого ключа
print(temp.get("name1111", "нет такого ключа"))

a = temp.get("name1", "Vlad")  # Vlad -дефолтное значение
print(a)
