# To open the file, use the built-in open() function.
# The open() function returns a file object,
# which has a read() method for reading the content of the file
file = 'myfile.txt'
f = open(file)
content = f.read()
print(content)
f.close()

f1 = open("Ex2_file_read_part.py")
print(f1.read())
f1.close()
