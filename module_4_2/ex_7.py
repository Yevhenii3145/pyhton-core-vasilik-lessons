string = "ndfig6g4fh 5 5 f h 2 jg33 ff! k 9"

new_list = [item for item in string if item.isdigit()]
new_list = [item for item in string if "0" <= item <= "9"]
print(new_list)

# Заполнить список числами которые кратные 30 или 31 в диапазоне 20..250
list = [item for item in range(20, 251) if item % 30 == 0 or item % 31 == 0]
print(list)
