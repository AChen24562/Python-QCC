def main():
    filename = 'Presidents3.txt'
    appending_files(filename)


def appending_files(filename):
    with open(filename, 'a') as afile:
        afile.write('J.M.\n')

        list = ['J.ME.', 'J.Q.A.']
        for i in range(len(list)):
            list[i] = list[i] + '\n'
        afile.writelines(list)


main()
