filename = "learning_python.txt"  # Reading file
fileout = "learning_C.txt"  # Writing file

# Open read file and read
with open(filename) as file:
    lines = file.readlines()
    print("Python version:")
    for content in lines:
        print(content.rstrip())


# Open writing file and write reading file replacing python with c++
print("\nC++ Version, and write file")
with open(fileout, 'w') as fout:
    for line in lines:
        line = line.rstrip()
        print(line.replace('Python', 'C++'))

        fout.write(f"{line.replace('Python', 'C++')}\n")
