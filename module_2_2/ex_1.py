first = int(input("Enter the first number"))
second = int(input("Enter the second number"))

if first > second:
    print("The first number is greater than the second number")
elif first == second:
    print("The first number equal the second number")
else:
    print("The first number is less than the second number")

if first % 2:
    print("The first number is odd")
else:
    print("The first number is even")
if second % 3:
    print("The second number is not divisible by three")
else:
    print("The second number is divisible by three")
