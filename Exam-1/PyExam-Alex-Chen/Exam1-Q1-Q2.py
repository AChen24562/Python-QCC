# 1 Create list comprehension of all numbers 1 - 200
list = [x for x in range(1, 201)]
print(list, "\n")

# 2 Request full name, display  first name last name, Initials capitalize
full_name = input("Enter your full name: ")
name_split = full_name.split()
print(f"First name: {name_split[0].title()}")
print(f"Last Name: {name_split[1].title()}")
print(f"Initials: {name_split[0][0].title()}.{name_split[1][0].title()}.")
