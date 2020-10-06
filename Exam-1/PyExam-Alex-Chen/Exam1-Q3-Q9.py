# 3 ONE LINE integer division, float division 2 decimals, modulus division
x = 5
y = 3

print(f"{x//y}\n{round(x/y, 2)}\n{x%y}")

# 4 ONE LINE final cost, and cost of items
pens = 4.95
pencils = 1.1
print(f"Pens: ${pens} Pencils: ${pencils:.2f} Total: ${pens + pencils:.2f}")

# 5 ONE LINE print max and min of list
num = [5, 0, 99, 0, 6]
print(f"Largest = {max(num)}\nSmalles = {min(num)}")

# 6 ONE LINE print value of gpa and type of variable
gpa = 99.99
print(f"{gpa}\n{type(gpa)}")

# 7 ONE LINE create two variables car1 car2 = Volvo, BMW
car1, car2 = "Volvo", "BMW"
print(car1, car2)

# 8 for loop to print list, seperated by tab + 10, new line
list = [0, 2, 4, 6, 8]
for x in list:
    print(x, "\t", x + 10)

# 9 request integer, display value of 1 + 1/2.. 1/n to five decimal places
# Display average of value to 5 decimals
num = int(input("Enter an integer: "))
sum = 0
counter = 0
for x in range(1, num + 1):
    sum += 1/x
    counter += 1

print(f"Sum: {sum:.5f}")
print(f"Average: {sum / counter:.5}")
