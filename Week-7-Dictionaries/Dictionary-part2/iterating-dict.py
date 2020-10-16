student_info = {'name': "John Smith",
                'GPA': 3.456,
                'Age': 20}

for keys, values in student_info.items():
    print(keys, "\t", values)

print()

student_info.update({"GPA": 4.0})

print()
for keys, values in student_info.items():
    print(keys, "\t", values)

print()
student_info['Major'] = 'CSIS'
for values in student_info.values():
    print(values, end="|")
print()


del student_info['GPA']
del student_info['Age']
print(student_info)
