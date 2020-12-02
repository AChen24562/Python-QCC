filename = 'learning_python.txt'

print("1st read all")
with open(filename) as file:
    contents = file.read()
print(contents)

print("2nd Read loop lines")
with open(filename) as file:
    for line in file:
        print(line.rstrip())

print("\n3rd Read storing then looping")
with open(filename) as file:
    lines = file.readlines()

for lines in lines:
    print(lines.rstrip())
