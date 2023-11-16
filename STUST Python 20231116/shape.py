class Myshape:
    def __init__(self,side,length,width,radius):
        self.side=side
        self.length=length
        self.width=width
        self.radius=radius
        
    def square_area(self):
        return self.side * self.side
    
    def rectangle_area(self):
        return self.length * self.width
    
    def circle_area(self):
        return self.radius * self.radius * 3.14
    
square=Myshape.square_area(4,0,0,0)
rectangle=Myshape.rectangle_area(0,6,5,0)
circle=Myshape.circle_area(0,0,0,8)

print(f"正方形面積 {square}")
print(f"長方形面積 {rectangle}")
print(f"圓形面積 {circle}")