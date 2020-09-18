# S. Trowbridge/J. Sun 2020

item1 = "apple"
item2 = "pear"

cost1 = 12.3456789
cost2 = 19.9595

# zero-based numbering system - Numbering begins with zero instead of one
# string format() method
# order of arguments is the same
print( "I want to buy {} and {}."
.format(item1, item2) )
print( "I want to buy {} and {}."
.format(item2, item1) )

# order of arguments is different (use indexes)
print( "I want to buy {1} and {0}.".format(item1, item2) )
print( "I want to buy {1} and {1}.".format(item1, item2) )
print("")

# width of 10 spaces for first parameter and precision of 2 for second parameter
#print( "{:10} {:10}{:.2f}".format(item1, "$", cost1) )
print( "{:10} {:10}{:.2f}".format(item1, "#", cost1) )
print("")

# set width, justification and precision for the same field
print( "{0:<10.3f} {2:<10} {1:10}".format(cost2, "1", item2))
print("")

# combine out-of-order, width, justification and precision
#print( "{1:10}{2:<15.2f} {0:10}".format(item1, "$", cost1) )
print( "{1:10} {2:<15.2f} {0:10}".format("$", item1, cost1) )
print("")
