sq_gen = (i ** 2 for i in range(10))
print(sq_gen)  # <generator object <genexpr> at 0x00000200347897D0>

# по одному и тому-же генератору можно проитерироваться только один раз
for i in sq_gen:
    print(i, end=" ")  # 0 1 4 9 16 25 36 49 64 81
print("")
