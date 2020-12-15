class Drink:
    def __init__(self, ounces):
        self.ounces = ounces

    def print_size(self):
        print(f"{self.ounces} ounces")


class Soda(Drink):
    def __init__(self, ounces, sugar):
        super().__init__(ounces)
        self.sugar = sugar

    def set_sugar(self, sugar):
        self.sugar = sugar

    def print_ounces_sugar(self):
        print(f"{self.ounces} ounces and {self.sugar} grams of sugar")


coke = Drink(12)
coke = Soda(12, 36)
coke. print_size()
coke.print_ounces_sugar()
