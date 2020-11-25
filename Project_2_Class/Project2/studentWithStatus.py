# Alex Chen
# Project 2 Classes
# Prof. Sun
# Answers are commented

class Student:  # Adds ID parameter
    def __init__(self, name="Anonymous", midterm=0, final=0, id=""):
        self._name = name
        self._midterm = midterm
        self._final = final
        self._semesterGrade = ""
        self._id = id

    def setName(self, name):
        self._name = name

    def setMidterm(self, midterm):
        self._midterm = midterm

    def setFinal(self, final):
        self._final = final

    def getName(self):
        return self._name


class LGstudent(Student):
    def __init__(self, name, midterm, final, id, inOutState):
        super().__init__(name, midterm, final, id)  # Uses parent def of parameters
        self._inOutState = inOutState  # Assigns state status

    def isInState(self):  # Checks whether student is intage and return T/F
        if self._inOutState.upper() == 'Y':
            return True
        else:
            return False

    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def __str__(self):
        if self.isInState():  # If isInState is True, print in state student
            return (self._name + "\t" + self._id + "\t" + self.calcSemGrade() +
                "\t" + "In-State Student")
        else:  # If isInState is False, print out state student
            return (self._name + "\t" + self._id + "\t" + self.calcSemGrade() +
                "\t" + "Out of state Student")

class PFstudent(Student):
    def __init__(self, name, midterm, final, id, fullTime=True):
        super().__init__(name, midterm, final, id)  # Use parent parameters
        self._fullTime = fullTime  # Initialize new  parameter fullTime

    def setFullTime(self, fullTime):
        self._fullTime = fullTime

    def getFullTime(self):
        return self._fullTime

    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2)
        if average >= 60:
            return "Pass"
        else:
            return "Fail"

    def isFullTime(self):  # Checks whether sudent is full or part, return T/F
        if self._fullTime.upper() == "Y":
            return True
        else:
            return False

    def __str__(self):
        if self.isFullTime():  # If T, print this
            return (self._name + "\t" + self._id + "\t" + self.calcSemGrade()
                 + "\t" + 'Full-Time Student')
        else:  #  If F, print this
            return (self._name + "\t" + self._id + "\t" + self.calcSemGrade()
                 + "\t" + 'Part-Time Student')


# New subclass for Intership Student
class InternshipStudent(PFstudent):
    def __init__(self, name, midterm, final, id, fullTime=True):
        name = "****"  # Set name to **** for internship students
        super().__init__(name, midterm, final, id, fullTime)  # Use parent parameters

# Remake calculation function
    def calcSemGrade(self):
        total = round(self._midterm + self._final)
        if total >= 100:
            return "S"
        else:
            return "U"

# Using parent's isFullTime() function for T/F
    def __str__(self):
        if self.isFullTime():  # If T, print this
            return (self._name + "\t" + self._id + "\t" + self.calcSemGrade()
                 + "\t" + 'Full-Time Student')
        else:  #  If F, print this
            return (self._name + "\t" + self._id + "\t" + self.calcSemGrade()
                 + "\t" + 'Part-Time Student')
