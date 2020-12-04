# By looping through the lines of the file,
# you can read the whole file, line by line.
# Loop through the file line by line
file = 'myfile.txt'
f = open(file)
for x in f:
    print(x)
f.close()
