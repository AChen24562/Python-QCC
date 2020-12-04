# You can return one line by using the readline() method.
# By calling readline() two times, you can read the two first lines.
file = 'myfile.txt'
f = open(file, "rt")
print("line 1:",f.readline())
print("line 2:",f.readline())
print("line 3:",f.readline())
print("line 4:",f.readline())
print("line 5:",f.readline())
f.close()
