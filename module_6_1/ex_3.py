import sys

NUMBER_LINES = 3

if len(sys.argv) != 2:
    print("Нужно добавить имя файла")
    quit()  # выход

try:
    file = open(sys.argv[1], "r", encoding="utf-8")
    count = 0
    while count < NUMBER_LINES:
        line = file.readline().strip()
        count += 1
        print(line)
    file.close()
except OSError as err:
    print(f"Ошибка доступа к файлу: {err}")
