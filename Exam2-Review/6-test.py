studInfo1 = {
    "Name": "Alex",
    "GPA": 3.0
}

studInfo2 = {
    "Name": "Wallard",
    "GPA": 2.5
}

studInfo3 = {
    "Name": "Albert",
    "GPA": 3.4
}

stuClass = []
stuClass.append(studInfo1)
stuClass.append(studInfo2)
stuClass.append(studInfo3)

for x in stuClass:
    print(x['Name'])
print()
for x in stuClass:
    print(x['GPA'])

print()
stuClass[2]['GPA'] = 4.0
for x in stuClass:
    for value in x.values():
        print(value, end=" ")
    print()
