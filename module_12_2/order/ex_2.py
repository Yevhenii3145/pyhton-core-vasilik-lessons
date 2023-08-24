# Распечатка и нумерация строк в текстовом файле
import pickle


class TextReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, encoding="utf-8")
        self.line_count = 0

    def read_line(self):
        self.line_count += 1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith("\n"):
            line = line[:-1]
        return "%i: %s" % (self.line_count, line)

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["file"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        file = open(self.filename, encoding="utf-8")
        for _ in range(self.line_count):
            file.readline()
        self.file = file


reader = TextReader("song.txt")
print(reader.read_line())
print(reader.read_line())
print(reader.read_line())
print("********")

new_reader = pickle.loads(pickle.dumps(reader))
while True:
    line = new_reader.read_line()
    if line is None:
        break
    else:
        print(line)

print("-------")
print(reader.read_line())
print(reader.read_line())
