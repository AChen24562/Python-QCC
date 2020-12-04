# It is a good practice to always close the file when you are done with it.
# Close the file when you are finish with it
file = 'myfile.txt'
f = open(file)
print(f.readline())
print(f.readline())
f.close()
