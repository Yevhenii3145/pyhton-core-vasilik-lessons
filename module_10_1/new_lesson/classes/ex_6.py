"""
Method Resolution Order (MRO).
MRO в Python работает слудующим образом:

1.Ищет атрибут среди атрибутов самого класса. Именно благодаря этому вы можете "переопределить" родительские атрибуты.
2.Ищет атрибут у первого из родителей (тот, который указан первым в списке родителей).
3.Ищет атрибут у следующего родителя в списке родителей, пока такие есть.
4.Ищет атрибут в родителях первого из родителей.
5.Повторяет п.4 по всем родителям.
6.Вызывает исключение, что атрибут не найден.
"""

class A:
    def hi(self):
        print("A")

class B(A):
    # def hi(self):
    #     print("B")
    pass

class C(A):
    # def hi(self):
    #     print("C")
    pass

class D(B,C):
    # def hi(self):
    #     return 5 + 6
    pass

d = D()
d.hi() # A
print(D.__mro__) # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)