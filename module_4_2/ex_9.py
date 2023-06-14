import os
from pathlib import *

current_dir = Path.cwd()
home_dir = Path.home()

print(current_dir)
print(home_dir)

# outhpath = os.path.join(os.getcwd(), "output")
# outhpath_file = os.path.join(outhpath, "new_file.txt")

outhpath = Path.cwd() / "output" / "new_file.txt"
print(outhpath)

a = Path("diretory", "new.txt")
print(a)  # путь к файлу
print(a.name)  # имя файла
print(a.suffix)  # разширение
