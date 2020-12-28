def main():
    append_file = 'Presidents3.txt'
    appending(append_file)


def appending(append_file):
    list = ['James Madison', "James Monroe", "John Q. Adams"]
    with open(append_file, 'a') as append:
        for i in range(len(list)):
            list[i] = list[i] + "\n"
        append.writelines(list)


main()
