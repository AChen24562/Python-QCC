# Exercise number 4
courses = ['ET 585', 'ET 574', 'MA 471']

print(courses)

print(f"\nI have {len(courses)} courses\n")
print(f"First Course: {courses[0]}")
print(f"Last Course: {courses[-1]}\n\n")


# Exercise number 5
# a - c
n = []
n.append(2)
n.append(4)
print(n)

# d - g
n.insert(0, 0)
n.insert(1, 1)
n.insert(3, 3)
n.insert(5, 5)
print(n)

del n[0]
print(n)
digit_2 = n.pop(1)
print(digit_2)
