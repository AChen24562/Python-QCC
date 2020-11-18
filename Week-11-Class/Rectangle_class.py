from math import pi


class Rectangle:

    def __init__(self, width = 1, height=1):
        self.width = width
        self.height = height

# Set new width/height
    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

# Display Info
    def getWidth(self):
        print(f"New Width is: {self.width}")

    def getHeight(self):
        print(f"New Height is: {self.height}")

    def display(self):
        dimension = f"Width: {self.width}\nHeight: {self.height}"
        return dimension

# Area
    def area(self):
        print(f"Area of a Rectangle H:{self.height} x W:{self.width} = {self.height * self.width}")


class Circle:

    def __init__(self, radius=1):
        self.radius = radius

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        print(f"Radius is: {self.radius}")

    def area(self):
        area = pi * self.radius ** 2
        print(f"Area of circle with radius '{self.radius}' is {round(area,2)}")

    def circumference(self):
        circumference = 2 * pi * self.radius
        print(f"circumference with raidus '{self.radius} is {round(circumference, 2)}'")
