import math

class point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x, self.y)
    def move(self,x1,y1):
        self.x1=x1
        self.y1=y1
    def dist(self):
        print(math.sqrt(pow((self.x1 - self.x),2) + pow((self.y1 - self.y),2)))

x=point(int(input()),int(input()))
x.show()
x.move(int(input()),int(input()))
x.dist()
        
