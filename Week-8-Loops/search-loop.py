from math import floor

list = [1, 5, 6, 11, 12]

target = 5  # x
length = len(list)  # j (5)
beginning = 0  # i


while beginning < length:
    m = floor((beginning + length)/2)  # 2
    if target > list[m]:
        beginning = m + 1
    else:
        length = m
    print(m, length)

if target == list[m]:
    print(f"{target} is in position {m}")
else:
    print(f"{target} does not exist in {list}")
