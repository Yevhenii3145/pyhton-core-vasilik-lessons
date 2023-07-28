def factorial(n, cache={}):
    if n < 0:
            raise ValueError("Number can't be negative")

    def calc(n):
        result = 1
        for val in range(1, n + 1):
            if val in cache: # проверяем, есть ли результат в кэше
                result = cache[val] # берём результат из кэша
                print(f"{val} in cache {result}",end="  ")
            else:
                result = val * cache.get(val-1, 1) # чтобы не было ошибки добавим дефолт = 1
                cache[val] = result # присваиваю результат в словарь кэша
                print(f"{val} not in cache {result}",end="  ")
        return result
    return calc

f3 = factorial(3)
print(f"f(3): {f3(3)}") # 1 not in cache 1  2 not in cache 2  3 not in cache 6  f(3): 6

f5 = factorial(5)
print(f"f(5): {f3(5)}") # 1 in cache 1  2 in cache 2  3 in cache 6  4 not in cache 24  5 not in cache 120  f(5): 120

f4 = factorial(4)
print(f"f(4): {f3(4)}") # 1 in cache 1  2 in cache 2  3 in cache 6  4 in cache 24  f(4): 24
