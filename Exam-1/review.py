grades = []

for i in range(1, 4):
    input_grade = float(input(f"Enter a grade {i}: "))
    grades.append(input_grade)

print(f"\nOriginal List:\n{grades}")

grades.sort()
print(f"\nSorted list:\n{grades}")

print(f"\nMax = {max(grades)}")
print(f"\nMin = {min(grades)}")
print(f"\nSum = {sum(grades)}")
print(f"\nLength of List = {len(grades)}")
average = round(sum(grades) / len(grades))
print(f"\nAverage = {average}")
grades.append(average)

name = input("\nEnter your name: ")
grades.insert(0, name)
id = input("Enter your ID:")
grades.insert(1, "574-" + id)

print(f"\nFinal List:\n{grades}\nList type: {type(grades)}")
