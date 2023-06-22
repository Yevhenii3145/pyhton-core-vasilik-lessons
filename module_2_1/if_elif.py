# elif - если выполнится условие то интерпретатор остановится на нём и не пойдет дальше
# if - интерпретатор в любом случае пойдет проверять следующий if
a = 11
if a == 5:
    print("Var a equal: 5")
elif a == 6:
    print("Var a equal: 6")
elif a == 7:
    print("Var a equal: 7")
elif a == 8:
    print("Var a equal: 8")
# else выполнится если if или elif не выполнятся
else:
    # Var a is not equal: 5. It's: 11
    print(f"Var a is not equal: {5}. It's: {a}")

a = 55

if a == 55:
    print("Var a equal: 55")
if a > 5:
    print("Var a > 5")
if a >= 7:
    print("Var a >= 7")
if a >= 8:
    print("Var a >= 8")
else:
    print(f"Var a not > 5. It's: {a} ")
