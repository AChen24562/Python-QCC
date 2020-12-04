fileout = 'guest_book.txt'

while True:
    name = input('Enter your name: ')
    name = name.title()

    if name == 'Exit':
        print("Exiting....\n")
        exit()

    print(f"Welcome {name}!\n")
    try:
        with open(fileout, 'x') as fout:
            fout.write(f"{name}\n")
    except FileExistsError:
        with open(fileout, 'a') as fout:
            fout.write(f"{name}\n")
