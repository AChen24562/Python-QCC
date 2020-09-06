# Alex Chen
# Prof. Sun

chocolateBar = 2.75
potatoChip = 2.50
sugarCookie = 1.75
pretzel = 1.25

sales_tax = .0875
subtotal = chocolateBar + potatoChip + sugarCookie + pretzel
tax = sales_tax * subtotal


print("Chocolate Bar:\t", chocolateBar, "\n",
      "Potato Chips:\t", f"{potatoChip:.2f}", "\n",
      "Sugar Cookie:\t", sugarCookie, "\n",
      "Pretzel:\t", pretzel, "\n",
      "Subtotal:\t", subtotal, "\n",
      "Tax:\t\t", f"{tax:.2f}", "\n-------------------")

total = f"{subtotal + tax:.2f}"
print("Total: \t\t$", end="")
print(total, "\n")
