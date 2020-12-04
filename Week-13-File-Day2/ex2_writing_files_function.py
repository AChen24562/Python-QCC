def main():
    filename = 'Presidents2.txt'
    writing_file(filename)

    filename2 = 'President3.txt'
    write_file_lines(filename2)


def writing_file(filename):
    with open(filename, 'w') as out:
        out.write('George Washington\nJohn Adams')


def write_file_lines(filename):
    with open(filename, 'w') as out:
        list = ['George Washington', 'John Adams', 'Thomas Jefferson']

    # Or
        for i in range(len(list)):
            list[i] = list[i] + '\n'
        out.writelines(list)


main()
