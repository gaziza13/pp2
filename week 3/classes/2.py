class square():
    def __init__(self,len=0):
        self.len=len
    def area(self,len):
       print(self.len * self.len)


class shape(square):
    def __init__(self,len):
        self.len=len
    def area(self,len):
       print(self.len * self.len)

x=square()
x.area(0)
