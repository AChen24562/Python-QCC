class Student:

    def __init__(self, name='None', id=574):
        self.name = name
        self.id = id

    def display(self):
        prefix = 'QCC-000'
        print("Name:", self.name.title())
        print(f"ID: {prefix}{self.id}")
