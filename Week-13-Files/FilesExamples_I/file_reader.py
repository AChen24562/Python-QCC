filename = 'C:\\Users\\Alex\\Desktop\\Coding\\Python-QCC\\Week-13-Files\\FilesExamples_I\\pi_digits.txt'
# or 'pi_digits.py'

with open(filename) as file_object:
    lines = file_object.readlines()

print(lines)

for line in lines:
    print(line.rstrip())
print()
for line in lines:
    print(line.lstrip())
print()
for line in lines:
    print(line.strip())
print()
for line in lines:
    print(line)
