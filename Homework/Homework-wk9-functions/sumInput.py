# Alex Chen
# ET 574, Functions
# Hw #2
# Prof. Sun


def sumInput(num1):
    sum = 0
    list = []
    while num1 > 0:
        sum += num1
        list.append(num1)
        print(f"Sum: {sum}\n")
        num1 = eval(input("Enter a positive number to sun or a negative to end: "))
    else:
        print(f"All numbers: {list}\nEnding...")


num1 = eval(input("Enter a positive number to sun or a negative to end: "))
sumInput(num1)
