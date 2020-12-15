num = input("Enter a number 1 - 100: ")

try:
    num = float(num)
    if num >= 1 and num <= 100:
        print("Valid")
    else:
        print("Out of Range")
except ValueError:
    print("Invalid")
