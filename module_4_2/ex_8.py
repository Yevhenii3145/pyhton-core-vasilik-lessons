import os
print(os.path.join("usr", "bin", "media"))

print(os.getcwd())
# os.chdir("new/path") #поменять папку

# создаем папку в текущей директории
# os.makedirs('test')

# выведет путь к текущей папке
print(os.path.abspath("."))

# выведет аболютный путь к файлу
print(os.path.abspath("ex_1.py"))
print(os.path.isabs("ex_1.py"))  # False
os.path.relpath(path="C:\\Windows", start="C:\\")
