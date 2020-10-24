# Alex Chen
# ET 574
# Prof. Sun

print("USING WHILE LOOP\n")

# variables for start, stop, and increment values
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

increment = int(input("Enter a number to increment by: "))

# while start is less than or equal to stop run loop
while lower <= upper:
    print(lower)
    lower += increment


# Reset the original variables or use new ones
print("\nUSING FOR LOOP \n")
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

increment = int(input("Enter a number to increment by: "))
# for loop range(start, stop, step by)
for x in range(lower, upper + 1, increment):
    print(x)
