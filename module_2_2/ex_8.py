# находим индекс последнего вхождения для сивола "x"
string = input("Enter text: ")
index = -1
count = 0

for char in string:
    if char == "x":
        index = count
    count += 1
print(index)
