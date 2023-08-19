from time import time
# import resource


def read_file_yield(filename):
    text_file = open(filename, "r")
    while True:
        line = text_file.readline()
        if not line:
            text_file.close()
            break
        yield line


start = time()
data = read_file_yield("data.txt")
print(time() - start)  # 9.236466499604058e-07
# print("Peak Memory usage: ", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) 7 352 320
