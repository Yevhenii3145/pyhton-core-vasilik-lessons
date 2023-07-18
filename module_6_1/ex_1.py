file = open("test.txt", "w", encoding="utf-8")
print(type(file))  # <class '_io.TextIOWrapper'>
file.write("Hello world\n")
file.write("Hello world 1\n")
file.write("Hello world 2\n")
file.writelines(["Hi Jack\n", "Hi David\n", "Hi Bob\n"])
file.close()

file = open("test.txt", "r", encoding="utf-8")
# result = file.read()  # считывает сразу весь файл в память
# print(type(result))  # <class 'str'>
# print(result)

# result = file.readline()  # читает одну строку
# print(result) # Hello world

# читает все строки и записывает их в список
result = file.readlines()
# ['Hello world\n', 'Hello world 1\n', 'Hello world 2\n', 'Hi Jack\n', 'Hi David\n', 'Hi Bob\n']
print(result)
file.close()
