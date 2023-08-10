class Rectangle:
    def __init__(self, length,width):
        self.length = length
        self.width = width

    def perimetr(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def show(self):
        print("The length is ", self.length)
        print("The width ", self.width)
        print("The perimeter ", self.perimetr())
        print("The area ", self.area())


class Paralelepiped(Rectangle):
    def __init__(self,length,width,height):
        # Rectangle.__init__(self, length,width)
        super(Rectangle,self).__init__(length,width)
        self.height = height

    def l_w_h(self):
        return self.length * self.width * self.height

rectangle = Rectangle(5,6)
print(rectangle.show()) # The length is  5 The width  6 The perimeter  22 The area  30 None

paralelepiped = Paralelepiped(4,6,2)
print("PARALELEPIPED", paralelepiped.l_w_h()) # PARALELEPIPED 48
print(paralelepiped.perimetr())
print(paralelepiped.show())
