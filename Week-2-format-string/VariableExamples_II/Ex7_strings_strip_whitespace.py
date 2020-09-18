# S. Trowbridge/J.Sun 2020

name = "            Tom & Jerry        "
#name = name.rstrip()
#name = name.lstrip()
print(name)


# note the additional whitespace
print(name+" is a funny video.\n")

# rstrip removes white space from the RIGHT side of the string for the print command
print(name.rstrip()+" is a funny video.\n")

# note that rstrip did not change the value of the variable name
print(name+" is a funny video.\n")

# lstrip removes white space from the LEFT side of the string for the print command
print(name.lstrip()+" is a funny video.\n")

# note that lstrip also does not change the value of the variable name
print(name+" is a funny video.\n")
