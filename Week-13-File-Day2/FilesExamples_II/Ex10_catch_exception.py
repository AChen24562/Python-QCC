# Things can go wrong when you try to read and write files.
# If you try to open a file that doesn’t exist, you get an IOError.

# IOError: [Errno 2] No such file or directory

try:
    file = 'myfile.txt'
    fin = open(file,"r")
    for line in fin:
        print(line)
    fin.close()
except:
    print("Exceptions: Something went wrong.")

print("Hello World")
