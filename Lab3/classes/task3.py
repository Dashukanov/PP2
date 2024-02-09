class Shape:
    def __init__(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

rectangle = Rectangle(length = 5, width = 10)
area = rectangle.calculate_area()
print(f"Area of rectangle: {area}")