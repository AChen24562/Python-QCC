import studentWithStatus


def main():
    listOfStudents = obtainListOfStudents()  # students and grades
    displayResults(listOfStudents)


def obtainListOfStudents():
    listOfStudents = []
    carryOn = 'Y'
    while carryOn == 'Y':
        name = "alex"
        midterm = 100
        final = 100
        id = "123"
        category = "PF"

##
        if category.upper() == "LG":
            inOutState = "N"  ###
            st = studentWithStatus.LGstudent(name, midterm, final, id, inOutState)
        else:
            status = input("Is the student full time? (Y/N)")
            fullTime=False
            if status.upper() == 'Y':
                fullTime=True
            st = studentWithStatus.PFstudent(name, midterm, final, id, fullTime)

        listOfStudents.append(st)
        carryOn = "n"  ##
        carryOn = carryOn.upper()
    return listOfStudents


def displayResults(listOfStudents):
    print("\nNAME\tGRADE\tID\tSTATUS")
    listOfStudents.sort(key = lambda x: x.getName())
    for pupil in listOfStudents:
        print(pupil)


main()
