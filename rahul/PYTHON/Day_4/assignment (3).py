class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def findArea(self):
        area = self.length * self.width
        print("Area of a rectangle: ",area)
    
    def findPerimeter(self):
        perimeter = 2*(self.length + self.width)
        print("Perimeter of a rectangle: ",perimeter)
        
r1 = Rectangle(8,4)
r1.findArea()
r1.findPerimeter()