class MyException(Exception):
    def __init__(self,value):
        self.value = value



def baz(n: int):
    if n < 0:
        raise MyException(f"Value {n} < 0")
    else:
        return n + 5

print(baz(10)) # 15

try:
    print(baz(-10))
except MyException as err:
    print(err) # Value -10 < 0
