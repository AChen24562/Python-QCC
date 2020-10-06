vehicles = ['car', 'Truck', 'boat', 'PLANE']

print(vehicles, '\n')

letter = input("Enter a search letter: ")

if(len(letter) == 1):
    for x in vehicles:
        if(letter.lower() in x or letter.upper() in x):
            print(f"{x} contains '{letter}' and is in position {vehicles.index(x)}")
        else:
            print(f"{x} does not contain '{letter}'")
else:
    print("\nInvalid Search letter")
