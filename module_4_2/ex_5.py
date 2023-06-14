# dict_name = {new_key: new_value for item in iterable}

import random
users = ["Ivan", "Petr", "Oksana", "Irina", "Stas", "Igor"]
new_dict = {user: f"{random.randint(1, 30)} лет" for user in users}
print(new_dict)

users = ["Ivan", "Petr", "Oksana", "Irina", "Stas", "Igor"]
ages = [20, 35, 16, 18, 34, 20, 44, 444]

# лишние элементы будут просто откидаться
new_dict = {user: age for (user, age) in zip(users, ages)}
print(new_dict)


nums = [2, 3, 4, 5, 6, 7, 8]
test = {item: item ** 2 for item in nums if item % 2 == 0}
print(test)

t = {}
for n in nums:
    if n % 2 == 0:
        t[n] = pow(n, 2)
print(t)

q = {n: True if n % 2 == 0 else False for n in range(10)}
print(q)
