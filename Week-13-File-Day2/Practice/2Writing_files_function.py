def main():
    filename = 'Presidents2.txt'
    writing_file(filename)

    filename2 = 'Presidents3.txt'
    writing_file_lines(filename2)


def writing_file(filename):
    with open(filename, 'w') as outfile:
        outfile.write('G.W.\nJ.A.')


def writing_file_lines(filename):
    with open(filename, 'w') as outfile:
        list = ['G.W.', 'J.A.', 'T.J.']

        for i in range(len(list)):
            list[i] = list[i] + '\n'
        outfile.writelines(list)


main()
