num = int(input("Enter a number (-10, 10): "))

total = 0
while num >= -10 and num <= 10:
    total += num
    num = int(input("Enter a number (-10, 10): "))
else:
    print("Number out of range entered. Loop Terminated")
    print(f"Total: {total}")
