# To write to an existing file,
# you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

# Open the file and append content to the file:
file = 'myfile1.txt'
f = open(file, "a")
f.write("Now the file has more content!\n")
#f.close()

#Open and read the file after the appending:
f = open(file)
print(f.read())
f.close()
