class Quizzes(list):
    grade_list = []
    original_list = []

    def __init__(self, grade_list):
        self.grade_list = grade_list
        for i in self.grade_list:
            self.original_list.append(i)
        self.grade_list.remove(min(self.grade_list))

    def average(self):
        average = sum(self.grade_list) / len(self.grade_list)
        phrase = f"Quiz average: {average}"
        return phrase

    def display(self):
        print(f"\nOriginal Grades are: {self.original_list}")
        print(f"Updated Grades are:")
        for i in self.grade_list:
            print(f"Quiz 1: {i}")
        print()
