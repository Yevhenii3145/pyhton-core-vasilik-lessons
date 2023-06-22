# False , 0 , 0.0, "", None -> False
# Всё остальное -> True
a = True
b = 1
c = False
d = None

if a:  # a is True
    if b:
        if d:
            print("a -> b ->d")
        # ВЫПОЛНИТСЯ ТОЛЬКО ЭТО УСЛОВИЕ
        elif not d:
            print("a -> b -> not d")  # a -> b -> not d
        elif not c:
            if b:
                print("a -> b -> not c")
        else:
            print("else")
elif b:  # сюда в итоге интерпретатор даже не зайдет
    print("b")
elif not c:
    print("not c")
else:
    print("No idea")
