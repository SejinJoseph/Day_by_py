class Shapes:
    def __init__(self,color,is_filled):

        self.color=color
        self.is_filled=is_filled

    def describe(self):
        print(f"Color: {self.color}")
        print(f"Filled: {self.is_filled}")

class Circle(Shapes):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius
        
    def describe(self):
        super().describe()
        print(f"It is a Circle with radius: {self.radius} and area: {3.14 * self.radius * self.radius}")

class Triangle(Shapes):
    def __init__(self,base,height,color,is_filled):
        super().__init__(color,is_filled)
        self.base=base
        self.height=height
        

    def describe(self):
        print(f"It Is a triangle with base:{self.base} and Height:{self.height} where the area:{(self.height*self.base)/2} ")


class Square(Shapes):
    def __init__(self, color, is_filled,length):
        super().__init__(color, is_filled)
        self.length=length

    def describe(self):
        super().describe()
        print(f"It is a square with length:{self.length} and Area :{self.length*self.length}")

circle=Circle(color="Red",is_filled="True",radius= 10 )
triangle=Triangle(color="green",is_filled="False",base= 10,height=17 )
square=Square(color="Red",is_filled="True",length= 10 )

circle.describe()
print()
triangle.describe()
print()
square.describe()
print()

print(circle.color)
