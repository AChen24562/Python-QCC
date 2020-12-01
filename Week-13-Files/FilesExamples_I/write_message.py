filename = 'programming.txt'

with open(filename, 'r+') as file_object:
    file_object.write(" Hi Python\n")

with open(filename, 'w') as file_object:
    file_object.write("I loving programming.\n")
    file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
