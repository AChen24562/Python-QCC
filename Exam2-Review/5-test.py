studInfo = {
    "Name": "Alex",
    "GPA": 3.0,
    "Age": 20
}

for keys, values in studInfo.items():
    print(keys, values)

studInfo.update({'GPA': 4.0})
print(studInfo)

for x in studInfo.keys():
    print(x, studInfo[x])

studInfo["Major"] = 'CSIS'
print()
for value in studInfo.values():
    print(value)

del studInfo['GPA']
del studInfo['Age']
print(f"\n{studInfo}")
