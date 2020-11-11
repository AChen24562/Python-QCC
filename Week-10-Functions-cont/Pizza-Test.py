from MakePizza import namesOfPizza as nOP
from MakePizza import make


def selection():
    choice = int(input("Select Pizza:\n1) Pepperoni\nChoice: "))
    return choice


nOP(selection())
make(12, "Pepperoni", "Cheese", "Tomato Sauce")
