hourlywage = float(input("Enter hourly wage: "))
hoursWorked = float(input("Enter number of hours worked: "))
totalwage = hourlywage * hoursWorked

print(hourlywage)
print(hoursWorked)

if(hoursWorked > 40):
    overtimeWage = (40 * hourlywage) + (1.5 * hourlywage * (hoursWorked - 40))
    print(f"Gross pay for week is: ${overtimeWage:.2f}")
else:
    print(f"Gross pay for week is: {totalwage:.2f}")
