class Square:
    def __init__(self, length ):
        self.length  = length

    def area (self):
        print(self.length * self.length == 0)  

class Shape(Square):
    def __init__(self, length = 0 ):
        self.length  = length
    
    def area (self) :
        print(self.length * self.length)        


class Rectangle(Shape):

    def __init__(self,  width):
        self.width = width

    def area (self, w):
        print( self.length  * w)  
        
t = Square(8)
Shape.area(t)

Rectangle.area(t,5)