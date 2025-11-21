class shape:
    def perimeter(self):
        pass
class Rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def perimeter(self):
        return 2*(self.legth+self.breadth)
class Circle(shape):
    def __init__(self,radius):
        self.radius=radius

    def primeter(self):
        return 2*3.14159*self.radius

class Square(shape):
    def __init__(self,side):
        self.side=side

    def perimeter(self):
        return 4*self.side



    #Function demonstrating polymorphism
    def show__perimeter(shape):
        print("perimeter",shape.perimeter())

    #Create object of different shapes
        rect=Rctangle(10,5)
        circle=Circle(3)
        square=Square(6)
    #polymorphis in action
        show_perimeter(rect)
        show_perimeter(circle)
        show_perimeter(square)
