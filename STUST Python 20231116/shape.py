class Myshape:
    def __init__(self,side,length,width,radius):
        self.side=side
        self.length=length
        self.width=width
        self.radius=radius
    #計算正方形面積 邊長 * 邊長
    def square_area(self):
        return self.side * self.side
    #計算長方形面積 長 * 寬
    def rectangle_area(self):
        return self.length * self.width
    #計算圓面積 半徑 * 半徑 * π(取3.14)
    def circle_area(self):
        return self.radius * self.radius * 3.14 
#設定邊長 = 4 , 長度 = 6 , 寬長 = 5 , 半徑 = 8
my_shape = Myshape(side=4, length=6, width=5, radius=8)

square = my_shape.square_area()
rectangle = my_shape.rectangle_area()
circle = my_shape.circle_area()

print(f"正方形面積 {square}")
print(f"長方形面積 {rectangle}")
print(f"圓形面積 {circle}")