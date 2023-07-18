import random

random.seed()
print(random.random()) # 0.6734695861129335
print(random.randint(1, 10)) # 8

for _ in range(10):
    # 10 не входит
    print(random.randrange(1, 10), end=" ") # 3 3 5 9 2 3 7 4 7 8

print("")
for _ in range(10):
    # 10 входит
    print(random.randint(1,10),end=" ") # 3 6 10 4 7 9 5 1 2 2
