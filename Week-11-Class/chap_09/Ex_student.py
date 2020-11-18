# To understand the meaning of classes
# we have to understand the built-in __init__() function.
# All classes have a function called __init__(),
# which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties,
# or other operations that are necessary to do when the object is being created.


class Student:
    # Create a class named Student,
    # use the __init__() function to assign values for name and id

    def __init__(self, name='None', id=574):
        self.name = name
        self.id = id

    def display(self):
        prefix = 'QCC-000'
        print("Name:",self.name.title())
        print(f"Id: {prefix}{self.id}")

s1 = Student("john smith",123456)
s1.display()
s2 = Student()
s2.display()
s2 = Student('tom')
s2.display()
