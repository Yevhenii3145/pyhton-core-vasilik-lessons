"""
Для того, чтобы объект можно было использовать в контсрукции with... as....: в объекте
должны быть методы: __enter__, __exit__.
__enter__ -- метод, который принимает только один аргумент self. Если метод что-то
возвращает, его вывод будет записан в переменную val в конструкции with context_manager
as val:.
__exit__ -- обязательно принимает 4 аргумента: self, exception type, exception value,
exception traceback.
Эти аргументы необходимы для корректной обработки исключений внутри __exit__.
"""


class FileWriter:
    def __init__(self, filename):
        self.file = None
        self.opened = False
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w")
        self.opened = True
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.opened:
            self.file.close()
        self.opened = False


if __name__ == "__main__":
    with FileWriter("new_file.txt") as f:
        f.write("Hello world\n")
        f.write("Happy lesson\n")
