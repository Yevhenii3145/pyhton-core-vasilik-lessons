def my_range(limit):
    value = 0
    while value < limit:
        yield value
        value += 1  # value = value + 1


for num in range(5):
    print(num, end=" ")  # 0 1 2 3 4
print("")

for num in my_range(5):
    print(num, end=" ")  # 0 1 2 3 4
print(" ")

gen = my_range(5)

while True:
    try:
        r = next(gen)
        print(r, end=" ")  # 0 1 2 3 4
    except StopIteration:
        break
print(" ")
