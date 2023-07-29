names = ["ivan", "petro", "oksana", "iryna"]


def normalize(name):
    return name.title()


# 1
new_name = []
for name in names:
    new_name.append(name.title())
print(new_name)  # ['Ivan', 'Petro', 'Oksana', 'Iryna']

# 2
new_name = map(normalize, names)
print(new_name)  # <map object at 0x0000020E8DCFB9D0>
print(list(new_name))  # ['Ivan', 'Petro', 'Oksana', 'Iryna']

# 3
new_name = map(str.title, names)
print(list(new_name))  # ['Ivan', 'Petro', 'Oksana', 'Iryna']


# 4
new_name = map(lambda name: name.title(), names)
print(list(new_name))

# 5
new_name = [name.title() for name in names]
print(new_name)  # ['Ivan', 'Petro', 'Oksana', 'Iryna']
