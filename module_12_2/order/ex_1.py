# Реализовать pickable класс, который сохраняет дату и время когда обьект
# этого класса  сериализовали и когда распаковали
import pickle
from time import sleep
from datetime import datetime


class RememberAll:
    def __init__(self, *args):
        self.data = list(args)
        self.saved = None
        self.restored = None

    def __getstate__(self):
        state = self.__dict__.copy()
        # state: {'data': [1, 2, 3, 4, 5], 'saved': None, 'restored': None}
        print(f"state: {state}")
        state["saved"] = datetime.now()
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.restored = datetime.now()


if __name__ == "__main__":
    print(RememberAll.__dict__)  # {'__module__': '__main__', '__init__': <function RememberAll.__init__ at 0x0000021FEB74CF40>, '__getstate__': <function RememberAll.__getstate__ at 0x0000021FEB74CE00>, '__dict__': <attribute '__dict__' of 'RememberAll' objects>, '__weakref__': <attribute '__weakref__' of 'RememberAll' objects>, '__doc__': None}
    r = RememberAll(1, 2, 3, 4, 5)
    print(r.data)  # [1, 2, 3, 4, 5]
    r_dump = pickle.dumps(r)
    sleep(3)
    r_load = pickle.loads(r_dump)
    print(r.saved, r.restored)  # None None
    # 2023-08-24 10:57:09.147413 2023-08-24 10:57:12.147782
    print(r_load.saved, r_load.restored)
