from math import floor

list = [1, 3, 5, 6, 12]

beginning = 0  # i
length = len(list)  # j

target = int(input(f"Enter a number to search for in, {list}: "))

while beginning < length:
    middle = floor((beginning + length)/2)
    if target > list[middle]:
        beginning = middle + 1
    elif target == list[middle]:
        break
    else:
        length = middle


if target == list[middle]:
    print(f"{target} is in index {middle}")
else:
    print(f"{target} does not exist in {list}")
