def main():
    output1 = 'Presidents2.txt'
    output2 = 'Presidents3.txt'

    writing_file(output1)
    writing_file_list(output2)


def writing_file(output1):
    with open(output1, 'w') as output:
        output.write('George Washing\nJohn Adams')


def writing_file_list(output2):
    list = ["George Washington", "John Adams", "Thomas Jefferson"]
    with open(output2, 'w') as output:
        for i in range(len(list)):
            list[i] = list[i] + "\n"
        output.writelines(list)


main()
