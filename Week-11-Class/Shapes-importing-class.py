from Shapes_Class import Rectangle, Circle

r1 = Rectangle(5, 3)
print(r1.display())
r1.area()

# Set new Width and print width
print()
r1.setWidth(2)
r1.getWidth()


# Set new Height and print height
r1.setHeight(7)
r1.getHeight()


print()
print(r1.display())
r1.area()


# Circle
# ---------------------------------
# When Circle Radius is default
print("\nCircle:")
c1 = Circle()
c1.getRadius()
c1.area()
c1.circumference()

print()
# Circle radius set to 5
c1.setRadius(5)
c1.getRadius()
c1.area()
c1.circumference()
