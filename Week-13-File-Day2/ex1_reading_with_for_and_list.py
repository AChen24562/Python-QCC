def main():
    file = "FirstPresidents.txt"
    displaywithloop(file)
    print()
    displaywithlist(file)


def displaywithloop(file):
    print("For loop:")
    with open(file) as president:
        for line in president:
            print(line.rstrip())


def displaywithlist(file):
    print("\nList:")
    with open(file) as president:
        list = president.readlines()
        for content in list:
            print(content.rstrip())

    infile = open(file, 'r')
    listPres = [line[:-1] for line in infile]
    print(listPres)
    infile.close()


main()
