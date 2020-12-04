def main():
    filename = 'President3.txt'
    appending_file(filename)


def appending_file(filename):
    with open(filename, 'a') as afile:
        afile.write('James Madison\n')

        # or

        list = ['James Monroe', 'John Quincy Adams']
        for i in range(len(list)):
            list[i] = list[i] + '\n'
        afile.writelines(list)


main()
