# инкапсуляция
class Animal:
    def __init__(self, nickname, age, weight):
        self.__nickname = None
        self.__age = None
        self.__weight = None
        # вызываем в инициализаторе сеттеры
        self.name = nickname
        self.age = age
        self.weight = weight

    @property
    def name(self):
        return self.__nickname

    @name.setter
    def name(self, nickname):
        if len(nickname) > 0:
            self.__nickname = nickname
        else:
            raise ValueError("Animal should have the nickname!")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in list(range(0, 50)):
            self.__age = age
        else:
            raise ValueError("Animal age is broken!")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError("Animal should have a weight!")


dog = Animal("Rex", 3, 5)
print(dog.name, dog.age, dog.weight)  # Rex 3 5

# dog = Animal("Rex", 3, -5)  # ValueError: Animal should have a weight!
