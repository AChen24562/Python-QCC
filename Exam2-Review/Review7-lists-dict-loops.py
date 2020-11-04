studInfo1 = {"Name": "Alex",
             "GPA": 3.0}

studInfo2 = {"Name": "Rebecca",
             "GPA": 3.0}

studInfo3 = {"Name": "Jenny",
             "GPA": 3.0}

stuClass = []

stuClass.append(studInfo1)
stuClass.append(studInfo2)
stuClass.append(studInfo3)
print(stuClass)

print("\nNames")
for x in stuClass:
    print(x.get('Name'))

print("\nGPAs")
for x in stuClass:
    print(x.get('GPA'))

print('test', stuClass[2]['GPA'])
stuClass[2]['GPA'] = 4.0
print('\nChange Last Student GPA')
print(stuClass)

print("\nPrint all names/gpas")
for x in stuClass:
    for v in x.values():
        print(v)
