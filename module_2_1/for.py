fruit = "apple"
for char in fruit:
    print(char)

for _ in fruit:  # _ если само значение не интересует
    print("Hello world")

for item in range(5):  # start:stop:step  start по дефолту 0, тут стоп равен 5
    print(item, end="*")  # 0*1*2*3*4*
for item in range(1, 5, 2):
    print(item, end="*")  # 1*3*

for i, value in enumerate("new", 20):
    print(f"Iteration: {i} - Value = {value}")
# Iteration: 20 - Value = n
# Iteration: 21 - Value = e
# Iteration: 22 - Value = w
