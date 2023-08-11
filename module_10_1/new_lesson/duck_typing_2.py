class Duck:
    def swim_quack(self):
        print("I'm a duck and I can swim and quack")


class ToyBird:
    def swim_quack(self):
        print("I'm a duck and I can swim and quack")


class Fish:
    def swim(self):
        print("I can only swim")


def duck_testing(animal):
    try:
        animal.swim_quack()
    except AttributeError as er:
        print(f"It is not duck_typing! {er}")


# первые 2 обьекта это утиная типизация, а третий нет
duck_testing(Duck())  # I'm a duck and I can swim and quack
duck_testing(ToyBird())  # I'm a duck and I can swim and quack
# It is not duck_typing! 'Fish' object has no attribute 'swim_quack'
duck_testing(Fish())
