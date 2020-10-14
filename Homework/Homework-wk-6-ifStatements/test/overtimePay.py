hourlywage = float(input("Enter hourly wage: "))
hoursWorked = float(input("Enter number of hours worked: "))

if(hoursWorked > 40):
    overtimeWage = (40 * hourlywage) + (1.5 * hourlywage * (hoursWorked - 40))
    print(f"Gross pay for week is: ${overtimeWage:.2f}")
elif(hoursWorked < 40):
    weeklypay = hourlywage * hoursWorked
    print(f"Gross pay for week is: ${weeklypay:.2f}")
