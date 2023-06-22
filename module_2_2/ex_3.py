num = int(input("Enter number: "))

if not num % 2 and not num % 3:
    print("Чило кратное 2 и 3")
if not num % 3 and not num % 5:
    print("Чило кратное 3 и 5")

if num >= 10 and num <= 100:
    print("Число находится в промежутке 10...100")
