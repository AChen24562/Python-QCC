# To write to an existing file,
# you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

# Open the file and overwrite the content:
file = 'myfile2.txt'

f = open(file, "w")
f.write("Oops! I have deleted the content!")
#f.close()

#open and read the file after the appending:
with open(file) as f:
    print(f.read())
