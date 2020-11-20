from quizzes import Quizzes

list = []
for i in range(1, 7):
    list.append(eval(input(f"Enter grade on Quiz {i}: ")))


quizGrades = Quizzes(list)
quizGrades.display()
print(quizGrades.average())
