# SOLID
# DRY - don't repeat your self

class Dog(object):
    """This is a dog model."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """The dog will sit"""
        print(self.name.title() + " is sitting now")

    def roll_over(self):
        """The dog is rolling over"""
        print(self.name.title() + " rolled over")

dog_jessie = Dog("jessie", 5)
print(dog_jessie) # <__main__.Dog object at 0x00000176746FCBD0>
print("My dog name is " + dog_jessie.name.title()) # My dog name is Jessie
print("My dog is " + str(dog_jessie.age) + " years old") # My dog is 5 years old
dog_jessie.sit() # Jessie is sitting now
dog_jessie.roll_over() # Jessie rolled over

my_dog = Dog("rex", 2)
print("My dog name is " + my_dog.name.title()) # My dog name is Rex
print("My dog is " + str(my_dog.age) + " years old") # My dog is 2 years old
my_dog.sit() # Rex is sitting now
my_dog.roll_over() # Rex rolled over
