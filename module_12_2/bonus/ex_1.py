import shelve


class TestClass:
    awesome = True


class DummyClass:
    default = 0

    def __init__(self, value):
        self.default = value


aw = TestClass()
dum = DummyClass(42)
filename = "some_db"

with shelve.open(filename) as db:
    db['test'] = aw
    db['dummy'] = dum
    db['my_list'] = [1, 2, 3, 4]
    temp = db['my_list']
    temp.append(5)
    db['my_list'] = temp

    daw = db['test']
    del db['test']


with shelve.open(filename) as states:
    for key in states:
        print(f'{key}: {states[key]}')  # my_list: [1, 2, 3, 4, 5]
    print(states['my_list'])  # [1, 2, 3, 4, 5]
    print(states['dummy'].default)  # 42
