from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Pizza(Circle):
    def __init__(self,topping,radius):
        super(). __init__(radius)
        self.topping=topping
    


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [ Circle(3),Triangle(5, 4), Square(10),Pizza("cheese",6)]

for shape in shapes:
    print(f"{shape.area()} cm²")