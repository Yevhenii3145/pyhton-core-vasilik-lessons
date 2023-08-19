"""
Разбераем разницу между: обычным методом, @classmethod и @staticmethod

@staticmethod используется в том случае, если ваш метод не имеет вообще доступа к классу или объекту класса.

@classmethod Методы класса принимают класс как параметр, который принято обозначать cls.
Он указывает на сам класс, а не на обьект этого класса
"""


class Test:
    def doubler(self, x):  # self == obj
        print("Mul on 2")
        return x * 2

    @staticmethod
    def triples(x):
        print("Mul on 3")
        return x * 3

    @classmethod
    def quad(cls, x):  # cls == Test
        print("Mul on 4")
        return x * 4


obj = Test()
print("---Экземпляр класса---")
print(obj.doubler(4))  # Mul on 2  8
print(obj.triples(4))  # Mul on 3  12
print(obj.quad(4))  # Mul on 4  16
print("---Вызов через класс---")
# TypeError: Test.doubler() missing 1 required positional argument: 'x'
# print(Test.doubler(4))
print(Test.triples(4))
print(Test.quad(4))
