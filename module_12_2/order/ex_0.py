import pickle


class A:
    def __init__(self, important_data):
        self.important_data = important_data

        self.func = lambda: 7  # не может сериализовать

        self.is_up = False  # не хотим сериализовать

    def __getstate__(self):
        return [self.important_data, self.is_up]

    def __setstate__(self, state):
        self.important_data = state[0]
        self.func = lambda: 7
        self.is_up = state[1]


a1 = A("Very important text")
ser = pickle.dumps(a1)

a2 = pickle.loads(ser)
print(a2)  # <__main__.A object at 0x00000189E053D8D0>
print(a2.important_data)  # Very important text
print(a2.func())  # 7
print(a2.is_up)  # False
