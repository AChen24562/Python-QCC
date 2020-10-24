from math import floor

list = [1, 5, 6, 11, 12]

target = 11
length = len(list)
print(length)

beginning = 1
while beginning < length:
    m = floor((beginning + length)/2)
    break
print(m)
