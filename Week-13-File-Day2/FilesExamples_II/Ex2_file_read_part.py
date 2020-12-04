# By default the read() method returns the whole text,
# but you can also specify how many characters you want to return:
# Return the 5 first characters of the file:
file = 'myfile.txt'
f = open(file, "r")
print(f.read(5))
f.close()
