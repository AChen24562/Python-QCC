import random
grades = []
passing_grade = []

amount = int(input("# of grades in list: "))
passing = int(input("Enter the passing grade: "))

for x in range(amount):
    rand = random.randint(1, 100)
    grades.append(rand)
    if rand >= passing:
        passing_grade.append(rand)

print(f"Original: {grades}")
print(f"Passing: {passing_grade}")
