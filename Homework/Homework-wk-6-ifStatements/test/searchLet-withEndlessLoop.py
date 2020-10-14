vehicles = ['car', 'Truck', 'boat', 'PLANE']

print(f"vehicles = {vehicles}\n")
letter = input("Enter a search letter, or exit: ")

while letter.title() != "Exit":
    if(len(letter) > 1):
        print("Invalid search letter")
    else:
        for x in vehicles:
            if letter.lower() in x or letter.upper() in x:
                print(f"{x} contains {letter} it is in {vehicles.index(x)}")
            else:
                print(f"{x} does not contain {letter}")

    print(f"vehicles = {vehicles}\n")
    letter = input("Enter a search letter: ")

else:
    print("\nExiting..")
