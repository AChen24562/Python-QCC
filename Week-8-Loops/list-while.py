list = []
number = eval(input("Enter a number or 0 to stop: "))

while number != 0:
    list.append(number)
    number = eval(input("Enter a number or 0 to stop: "))
else:
    print(list)
print()
