import studentWithStatus

def main():
    listOfStudents = obtainListOfStudents()  # students and grades
    displayResults(listOfStudents)

def obtainListOfStudents():
    listOfStudents = []
    carryOn = 'Y'
    while carryOn == 'Y':
        name = input("Enter student's name: ")
        midterm = float(input("Enter student's grade on midterm exam: "))
        final = float(input("Enter student's grade on final exam: "))
        category = input("Enter category (LG or PF): ")
        if category.upper() == "LG":
            st = studentWithStatus.LGstudent(name, midterm, final)
        else:
            status = input("Is the student full time? (Y/N)")
            fullTime=False
            if status.upper() == 'Y':
                fullTime=True
            st = studentWithStatus.PFstudent(name, midterm, final, fullTime)

        listOfStudents.append(st)
        carryOn = input("Do you want to continue (Y/N)? ")
        carryOn = carryOn.upper()
    return listOfStudents

def displayResults(listOfStudents):
    print("\nNAME\tGRADE\tSTATUS")
    listOfStudents.sort(key = lambda x: x.getName())
    for pupil in listOfStudents:
        print(pupil)


main()
