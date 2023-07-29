def simple_generator():
    yield "First"  # yield == return
    yield "Second"


for r in simple_generator():
    print(r)  # First Second

gen = simple_generator()
print(gen)  # <generator object simple_generator at 0x0000014107688B40>

r = next(gen)
print(r)  # First

r = next(gen)
print(r)  # Second

# r = next(gen)
# print(r) # Traceback (most recent call last): StopIteration
