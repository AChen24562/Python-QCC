'''1) Request a float number user input, price, from the console.
2) Print "Price Matches" if the variable price is equal to a float number, 99.99.
3) Otherwise print "Price Not Found".
Example Output 1
Enter the search price: 99
Price Not Found

Example Output 2
Enter the search price: 99.99
Price Matches'''

price = float(input("Enter a search price: "))
if price == 99.99:
    print("Price Matches")
else:
    print("Price not Found")
