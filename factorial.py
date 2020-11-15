decimal_number = int(input("Enter a decimal number: "))
begin = 2  # Start at factorial 2

factorial = []
while decimal_number > 0:
    factorial.append(decimal_number % begin)
    decimal_number = int(decimal_number / begin)
    begin += 1

factorial = factorial[::-1]  # list must be reversed as input of 6 gives 001, rather 100
print(factorial)
