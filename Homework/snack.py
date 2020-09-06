cB = 2.75
poC = 2.50
suG = 1.75
pre = 1.25

# Constant
sales_tax = .0875

# Subtotal variable
subtotal = cB + poC + suG + pre
tax = subtotal * sales_tax

print("Chocolate Bar:\t", cB, "\n",
      "Potato Chips:\t", f"${poC:.2f}", "\n",
      "Sugar Cookie:\t", suG, "\n",
      "Pretzel:\t", pre, "\n",
      "Subtotal:\t", subtotal, "\n",
      "Tax:\t\t", f"${tax:.2f}", "\n-------------------")

total = subtotal + tax
print("Total:\t\t", total + 1)
