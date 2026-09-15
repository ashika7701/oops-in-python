class rectangle:
    def __init__(self,width,height):
        self.width=width
        self.length=height
    def area(self):
        print("area of the rectangle:",self.width*self.length)
    def perimetre(self):
        print("perimetre of the rectangle:",2+(self.width+self.length))
rec1=rectangle(78,100)
rec2=rectangle(20,108)
rec1.area()
rec2.perimetre()
