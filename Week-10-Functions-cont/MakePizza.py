def make(size, *toppings):
    print(f"{size}-in pizza with ", end="")
    length = len(toppings)
    for topping in toppings:
        print(topping, end=" ")
        length -= 1
        if length == 1:
            print("and ", end="")


def namesOfPizza(choice):
    if choice == 1:
        print("You have ordered the Pepperoni Pizza\n")
    else:
        print("Unavaiable")
