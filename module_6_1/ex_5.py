from pathlib import Path

folder = Path("./temp")
filename = folder / "temp.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
except OSError as err:
    print(f"Ошибка доступа к файлу: {err}")

finally:
    print("\nFile operation completed")
