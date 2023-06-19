from pathlib import Path

current_path = Path('.')
print(current_path)  # .
print(current_path.cwd())

file = current_path / "bin" / "utils" / "paint.drawio.svg"
print(file)  # bin\utils\paint.drawio.svg
print(current_path.joinpath("bin", "utils", "paint.drawio.swg"))

print(file.parts)  # ('bin', 'utils', 'paint.drawio.svg')
print(file.name)  # paint.drawio.svg
# print(file.name.split())  # ['paint.drawio.svg']
print(file.name.split(".")[0])  # paint

print(file.parent)  # bin\utils

print(file.suffix)  # .svg
print(file.suffixes)  # ['.drawio', '.svg']
