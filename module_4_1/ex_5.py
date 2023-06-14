# метод count
l = ["new", "new_1", "bbb", "new_2", "new_3", "new_4", "rr", "bbb"]

print("new_4" not in l)

print(l.count("new"))  # 1
print(l.count("bbb"))  # 2
print(l.count("aaaa"))  # 0
