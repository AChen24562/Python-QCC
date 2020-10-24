# Alex Chen
# Prof. Sun
# ET 574


grades = {'Exam 1': 85,
          'Exam 2': 99,
          'Exam 3': 100}

print(grades)

counter = 0
sum = 0
for x in grades.values():
    counter += 1
    sum += x

print(f"Average: {sum/counter:.2f}")
