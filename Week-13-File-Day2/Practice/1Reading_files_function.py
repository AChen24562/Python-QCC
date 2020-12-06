def main():
    filename = 'Presidents.txt'
    readWithLoop(filename)
    print()
    readWithList(filename)


def readWithLoop(filename):
    with open(filename) as inputfile:
        for lines in inputfile:
            print(lines.rstrip())


def readWithList(filename):
    with open(filename) as inputfile:
        list = inputfile.readlines()
        for lines in list:
            print(lines.rstrip())


main()
