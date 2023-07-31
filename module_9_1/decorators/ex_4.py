from time import time,sleep

def time_counter(func):
    def interval(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        diff = time() - start
        return result(), diff
    return interval

@time_counter
def factorial_with_cache(n, cache={}):
    if n < 0:
        raise ValueError("Number can't be negative")
    sleep(3)
    def calc():

        result = 1
        for val in range(1, n + 1):
            if val in cache:
                result = cache[val]
            else:
                result = val * cache.get(val - 1, 1)
                cache[val] = result
        sleep(3)
        return result
    return calc

result = factorial_with_cache(10)
print(result) # (3628800, 3.001091241836548)
