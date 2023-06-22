count = 0
# вечный цикл
while count < 10:  # while 1
    print("Hello world")
    count += 1  # count = count + 1

while True:  # while 1
    s = input("Please enter chr: ")
    if s == "q":
        break  # при вводе "q" цикл прервётся
    print(s)

print("Outside loop")

while True:  # while 1
    s = input("Please enter chr: ")
    if s == "q":
        continue  # при вводе "q" итерация прервется, но не цикл
    elif s == "6":
        break
    print(s)

print("Outside loop")

num = int(input("Enter the integer (0 to 100): "))
sum = 0

while num >= 0:
    sum += sum
    num -= 1
