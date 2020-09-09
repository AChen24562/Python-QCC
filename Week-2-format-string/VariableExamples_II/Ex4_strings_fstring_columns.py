# S. Trowbridge/J.Sun
# Using f-string to format columns

item1 = "Apple"
brand1 = "Gala"

item2 = "Pears"
brand2 = "European"

# align information into columns of specific width
# :10 indicates that the current field should have a column width of 10 characters
print(f"{item1:10}{brand1}")
print(f"{item2:10}{brand2}")

print("")

# two 10 character columns
# justify first column to the right, second column to the left
print(f"{item1:>10}{brand1:<10}")

# two 10 character columns
# justify first column to the left, second column to the right
print(f"{item2:<10}{brand2:>10}")
