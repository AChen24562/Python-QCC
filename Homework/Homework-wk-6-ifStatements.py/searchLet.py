# Alex Chen
# Prof. Sun
# ET 574
# If Statements

vehicles = ['car', 'Truck', 'boat', 'PLANE']

print(f"Vehicles = {vehicles}", '\n')

letter = input("Enter a search letter: ")

if(len(letter) == 1):
    for x in vehicles:
        if(letter.lower() in x or letter.upper() in x):
            print(f"{x} contains '{letter}' and is in position {vehicles.index(x)}")
        else:
            print(f"{x} does not contain '{letter}'")
else:
    print("\nInvalid Search letter")


# Alternative method, Does not retain case of original words
#  ie. Will print: plane does not have z, rather than 'PLANE'

# Set original list to lowercase
'''vehicles_lower = [lower.lower() for lower in vehicles]

if(len(letter) == 1):
    for x in vehicles_lower:
        if(letter.lower() in x):  # Set input to lowercase and check if letter exists
            print(f"{x} contains '{letter}' in position {vehicles_lower.index(x)}")
        else:  # If letter isn't in word print:
            print(f"{x} does not contain '{letter}'")

else:  # If letter input is longer than 1 word:
    print("Invalid search letter")
'''
