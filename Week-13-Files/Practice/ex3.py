fileout = "guest.txt"

name = input("Enter your name: ")

with open(fileout, 'x') as fout:
    fout.write(name)
