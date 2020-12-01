filename = 'learning_python.txt'
fileout = 'learning_c.txt'
fout = open(fileout, 'w')

with open(filename) as f:
    lines = f.readlines()


for line in lines:
    # Get rid of newline, then replace Python with C.
    line = line.rstrip()
    print(line.replace('Python', 'C'))
    fout.write(f"{line}'\n")

fout.close()
