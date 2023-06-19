from pathlib import Path

new_dir = Path("ABC")
# exist_ok=True - если папка уже сущетвует, то не будет ошибки при попытке создать новую
new_dir.mkdir(exist_ok=True)
# new_dir.mkdir() #  без параметра будет FileExistsError: [WinError 183] Невозможно создать файл, так как он уже существует: 'ABC'
# new_dir.rmdir()  # удаляет папку если она не пустая

# new_dir = Path("Test/Temp")
# new_dir.mkdir(exist_ok=True, parents=True) # создаем папку в папке Test/Temp

list_data = ["First Line", "Hello world", "Test", "happy"]

with open(new_dir / "data.txt", "w", encoding="utf-8") as file:
    for line in list_data:
        file.write(f"{line}\n")

with open(new_dir / "data.avi", "w", encoding="utf-8") as file:
    file.writelines(list_data)
