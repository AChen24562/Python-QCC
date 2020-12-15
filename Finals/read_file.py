# import os
filename = 'myFile.txt'

# filename = os.path.abspath('myfile.txt')
try:
    with open(filename) as read_file:
        print(read_file.read())
except FileNotFoundError:
    print("File is not found")
except:
    print("There is another issue")
