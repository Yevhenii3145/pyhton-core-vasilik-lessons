from time import time
# import resource  # (работает только на unix системах) библиотека для проверки количества использованной памяти


def read_file(filename):
    text_file = open(filename, "r")
    lines = text_file.readlines()
    text_file.close()
    return lines


start = time()

data = read_file("data.txt")
print(time() - start)  # 0.9574065208435059
# print("Peak Memory usage: ", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) 231 047 168
