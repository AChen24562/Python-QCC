# S. Trowbridge/J. Sun 2020
# Using f-strings
item1 = "apples"
item2 = "pears"
number = 574
shoppingList1 = "I want to buy "+ str(number) +item1+item2
shoppingList2 = "I want to buy ", number, item1,item2
print(shoppingList1)
# f-strings are used to format string content

message = f"I want to buy {number} {item1} and {item2}."
print(message)

message = f"Hi ET{number}!"
print(message)

 # string methods can be used upon variables
message = f"Hi, do you want to buy {number} {item1}?"
print(message)

 # f-strings can span multiple lines if paranthesis are used
name = (f"{item1.title()}"
        f" and {item2} are delicious.")
print(name)

print(f"{item2.title()}"
      f" and {item1} are delicious.")
