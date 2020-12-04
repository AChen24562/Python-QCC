# Create a file
file = 'newfile1.txt'
f = open(file, "x")     #[ErrNo 17] occurs if file exists
f.write('Hi\n')
# Write to a file
file = 'newfile2.txt'
f = open(file, "w")
f.write('Hi\nPython!\n')
# Write to a file
file = 'newfile1.txt'
f = open(file, "a")
f.write('Python!')
