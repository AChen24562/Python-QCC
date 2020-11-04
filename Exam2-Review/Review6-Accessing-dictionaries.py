studInfo = {
    "Name": "Alex",
    "GPA": 3.0,
    "Age": 20
}

print("Items:")
for keys, values in studInfo.items():
    print(keys, values)

print("\nUpdate")
studInfo.update({"GPA": 4.0})
print(studInfo)

print("\nKeys:")
for x in studInfo.keys():
    print(x, studInfo[x])

studInfo["Major"] = "CSIS"
print(studInfo)

print("\nValues()")
for x in studInfo.values():
    print(x)

print("\nDel Method")
del studInfo["Age"]
del studInfo["GPA"]
print(studInfo)
