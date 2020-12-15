def main():
    filename = 'Presidents.txt'
    read_with_loop(filename)
    read_with_list(filename)


def read_with_loop(filename):
    with open(filename) as read_file:
        for lines in read_file:
            print(lines.rstrip())


def read_with_list(filename):
    print("\nList")
    with open(filename) as read_file:
        list = read_file.readlines()
        for lines in list:
            print(lines.rstrip())

    file = open(filename, 'r')
    listPres = [line[:-1] for line in file]
    print(listPres)
    file.close()


main()
