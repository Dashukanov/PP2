class Shape:
    def __init__(self):
        pass

    def area(self):
        print("Area of the figure: 0")

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        area_value = self.length ** 2
        print(f"Area of the figure: {area_value}")

shape = Shape()
shape.area()

square = Square(5)
square.area()