# генераторы списков
# [expression for element in iter if condition]
a = ["abc", "dfg", "jgf", "rrr", "twe", "sdg", "rrr", "wer"]
b = [value for value in a if value != "rrr"]
print(b)

a = [pow(item, 2) for item in range(10) if item != 2]
print(a)
