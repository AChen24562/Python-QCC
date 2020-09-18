chocolateBar = 2.75
potatoChip = 2.50
sugarCookie = 1.75
pretzel = 1.25

sales_tax = .0875

subtotal = chocolateBar + potatoChip + sugarCookie + pretzel
tax = subtotal * sales_tax
total = subtotal + tax

print(f"""chocolate Bar:\t${chocolateBar}
Potatoe Chips:\t${potatoChip:.2f}
Sugar Cookie:\t${sugarCookie}
Pretzel:\t${pretzel}
Subtotal:\t${subtotal}
Tax:\t\t${round(tax, 2)}
-------------------------
Total:\t\t${round(total, 2)}""")
