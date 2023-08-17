from contextlib import contextmanager


@contextmanager
def manager_resource(*args, **kwargs):
    file_handler = open(*args, **kwargs)
    try:
        yield file_handler
    finally:
        file_handler.close()


with manager_resource("new_file.txt", "r", encoding="utf-8") as f:
    print(f.read())
