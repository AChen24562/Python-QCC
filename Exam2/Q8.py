''' Given:
lunch_order = {'food': 'pizza', 'price':9.99 }

1) Update the value of 'price' from 9.99 to 6.99 in the dictionary lunch_order.
2) Access the values in the dictionary lunch_order to print the following.
Example Output
Today's lunch special: Pizza $6.99.'''

lunch_order = {
    "Food": "Pizza",
    "Price": 9.99}
lunch_order["Price"] = 6.99
print(f"Today's lunch specal: {lunch_order['Food']} ${lunch_order['Price']}")
