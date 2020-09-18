# S. Trowbridge/J.Sun 2020

item1 = "Apple"
cost1 = 12.3456789
barcode1 = "14235643"

item2 = "Pears"
cost2 = 19.9595
barcode2 = "52345123"

tax = .0875

# combination of width, precision, justfication and calculations
print( '{0:8} {1:1}{2:10} {3:1}{4:<11} {5:1}{6:<5.2f}'
.format(item1, "#", barcode1, "$", cost1, "$", cost1*tax ) )
print("")

# combination of width, precision, justfication and calculations
print( '{0:8} {1:1}{2:10} {3:1}{4:<11} {5:1}{6:<5.2f}'.format(item2, "#", barcode2, "$", cost2, "$", cost2*tax ) )
print("")
