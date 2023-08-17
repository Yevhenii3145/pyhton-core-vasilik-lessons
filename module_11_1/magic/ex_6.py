# Функтор

class Count:
    def __init__(self, init_steps):
        self.steps = init_steps

    def __call__(self, *args, **kwargs):
        inc, = args  # запись равносильна inc = args[0]
        self.steps += inc

    def add_steps(self, steps_temp):
        self.steps += steps_temp
        return self.steps


count_step = Count(100)
count_step(25)
count_step(50)
print(count_step.steps)  # 175
count_step.add_steps(25)
print(count_step.steps)  # 200
