numbers = []

for item in range(21):
    if item % 2 == 0:
        numbers.append(item)
print(numbers)

numvers_1 = [item for item in range(21) if item % 2 == 0]
print(numvers_1)

names = ["Ivan", "Petr", "Oksana", "Irina", "Stas", "Igor"]
# проверка подстроки "а" в элеменете
new_names = [item for item in names if "a" in item]
print(new_names)
