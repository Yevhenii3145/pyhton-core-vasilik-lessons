num = int(input("Enter first number: "))
length = len(str(num))

if length == 2 and num % 2 == 0:
    print("Парное двухзначное число")
else:
    print("Не парное или не двухзначное число")
