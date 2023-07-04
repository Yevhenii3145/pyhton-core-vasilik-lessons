import argparse  # позволяет писать консольные программы
from pathlib import Path
from shutil import copyfile


parser = argparse.ArgumentParser(description="Sorting folder") # парсер командной строки, description -просто описание
# --source - это имя переменной(длинаая запись) -s -это имя переменной(короткая запись)
parser.add_argument("--source","-s", required=False, help="Source folder")
parser.add_argument("--output", "-o", default="dist", help="Output folder")

# parser.parse_args() - парсер  vars - возвращает словарь
args = vars(parser.parse_args())

source = args.get("source") # из словаря берём значение по ключу (ключ source)
output = args.get("output") # из словаря берём значение по ключу (ключ output)

print(source, output)

def read_folder(path:Path) -> None:
    print(f"path equal: {path}")
    for el in path.iterdir():
        print(f"element: {el}")
        if el.is_dir():
            read_folder(el)
        else:
            copy_file(el) # el -файл

def copy_file(file: Path) -> None:
    ext = file.suffix
    ext = ext[1:]
    new_path = output_folder / ext # output  ext => dist/png
    print(f"New_path: {new_path}")
    new_path.mkdir(exist_ok=True, parents=True) # создаём папку с нужным расширением (jpg, png, etc.)
    copyfile(file, new_path / file.name) #  копирование файла

output_folder = Path(output)
read_folder(Path(source)) # вызов (старт работы) функции read_folder
