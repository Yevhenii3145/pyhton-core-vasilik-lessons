n = input("Number: ")

min = int(n[0])
max = int(n[0])
sum = 0

for number in n:
    number = int(number)
    sum += number
    if number > max:
        max = number
    if number < min:
        min = number

print(f"Sum: {sum}, Max: {max}, Min: {min}")
