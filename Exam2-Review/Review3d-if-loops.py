#3d Loops and Input
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 < num2:
    while num1 <= num2:
        print(num1, end="|")
        num1 += 1
elif num1 > num2:
    for x in range(num1):
        print(num1, end="|")
        num1 -= 1
else:
    print(f"{num1} = {num2}")
