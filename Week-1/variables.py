
print('Alex')
print('Chen')

fruits = {'apple': 1.75,
        'Orange': 3.50,
        'Banana': 2.25}
total = 0
print("\nItem\t\tprice")
for fruit, price in fruits.items():
    print("%s\t\t $%.2f" % (fruit, price))
    total += price
print("----------\nTotal\t\t $%.2f" % (total))
