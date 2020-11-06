'''Given:
items = ['notebooks', 'pens', 'pencils', 'usb']
quantities = [10, 24, 16, 12]

1) Create a dictionary, supplies by using the two given lists above.
2) Use a loop to print all keys and values in the dictionary supplies.
3) Print the dictionary supplies.
Example Output
10 - NOTEBOOKS, 24 - PENS, 16 - PENCILS, 12 - USB,

 {'notebooks': 10, 'pens': 24, 'pencils': 16, 'usb': 12}'''

items = ['notebooks', 'pens', 'pencils', 'usb']
quantities = [10, 24, 16, 12]
supplies = dict(zip(items, quantities))
for items, quantities in supplies.items():
    print(f"{quantities} - {items.upper()}", end=", ")

print()
print(supplies)
