# Alex Chen
# Project 2 Classes
# Prof. Sun
# Answers are commented

import studentWithStatus


def main():
    listOfStudents = obtainListOfStudents()  # students and grades
    displayResults(listOfStudents)


def obtainListOfStudents():
    listOfStudents = []
    carryOn = 'Y'
    while carryOn == 'Y':
        name = input("Enter student's name: ")
        id = input("Enter ID: ")  # Asking for ID
        midterm = float(input("Enter student's grade on midterm exam: "))
        final = float(input("Enter student's grade on final exam: "))
        category = input("Enter category (LG, PF or IN): ")

        if category.upper() == "LG":
            inOutState = input("Is the student in-state?<Y/N> ")  # Askes for state status of student
            st = studentWithStatus.LGstudent(name, midterm, final, id, inOutState)
        elif category.upper() == "PF":
            fullTime = input("Is the student full time? (Y/N)")
            st = studentWithStatus.PFstudent(name, midterm, final, id, fullTime)
        else:
            fullTime = input("Is the student full time? (Y/N)")
            st = studentWithStatus.InternshipStudent(name, midterm, final, id, fullTime)

        listOfStudents.append(st)
        carryOn = input("\nDo you want to continue (Y/N)? ")
        carryOn = carryOn.upper()
    return listOfStudents


def displayResults(listOfStudents):
    print("\nNAME\tID\tGRADE\tSTATUS")
    listOfStudents.sort(key = lambda x: x.getName())
    for pupil in listOfStudents:
        print(pupil)


main()
