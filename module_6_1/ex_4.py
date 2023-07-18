import sys

NUMBER_LINES = 3

if len(sys.argv) != 2:
    print("Нужно добавить имя файла")
    quit()  # выход

try:
    lines = []
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        for line in file:  # заменяет file.readline()
            lines.append(line)
            # если длина списка больше константы
            if len(lines) > NUMBER_LINES:
                # то удаляем последнюю строку
                lines.pop(0)
    # последние 3 элемента так как цикл отработает полностью по всему файлу
    print(lines)  # ['Hi David\n', 'Hi Bob\n', 'New Line\n']
except OSError as err:
    print(f"Ошибка доступа к файлу: {err}")
