# Alex Chen
# Prof. Sun
# Et 574

# Create list of multiples of 4 from 0 - 40
mult_4 = []

for i in range(0, 41, 4):
    mult_4.append(i)

print(mult_4)


# Use for loop to insert into a new list
new_list = []
for x in mult_4:
    new_list.append(x//2)

print(new_list)


# Use slicing to inser to a third new list
new_list2 = []
sliced_list = new_list[-15: 15]
for x in sliced_list:
    new_list2.append(x//2)
print(new_list2)
