class Rectangle:

    def __init__(self, width = 1, height=1):
        self.width = width
        self.height = height

    def display(self):
        dimension = f"Width: {self.width}\nHeight: {self.height}\n"
        return dimension


r1 = Rectangle(4, 5)
r1.display()
