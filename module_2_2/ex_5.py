n = input("Number: ")
count = 0
for item in n:
    if item == "0":
        count += 1
print(count)
print("another way", n.count("0"))
