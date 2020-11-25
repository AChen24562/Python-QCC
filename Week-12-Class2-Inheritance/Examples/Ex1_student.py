class Student:
    # initializer method
    def __init__(self, name="None", midterm=0, final=0):
        self._name = name
        self._midterm = midterm
        self._final = final

    # mutator methods
    def setName(self, name):
        self._name = name
    def setMidterm(self, midterm):
        self._midterm = midterm
    def setFinal(self, final):
        self._final = final

    # accessor methods
    def getName(self):
        return self._name

    # state representation method
    def __str__(self):
        return self._name + "\n" + str(self._midterm) + "\n" + str(self._final)

s = Student()
print(s)

s1 = Student('john', 80, 90)
print(s1)

s2 = Student('sara', final=100)
print(s2)
