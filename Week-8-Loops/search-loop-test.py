from math import floor

list = [1, 3, 5, 6, 12]

beginning = 0  # i
length = len(list)  # j

target = 3

while beginning < length:
    middle = floor((beginning + length)/2)
    if target > list[middle]:
        beginning = middle + 1
    else:
        length = middle
    print(beginning, middle, length)

if target == list[middle]:
    print(f"{target} is in index: {middle}")
else:
    print(f"{target} does not exist in {list}")
