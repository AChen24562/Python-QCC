list = [x for x in range(1, 10)]

print(list)

even_nums = []
for even in range(2, 11, 2):
    even_nums.append(even)
print(even_nums)

squares = []
for values in range(1, 11):
    squares.append(values ** 2)
print(squares)

squares2 = [x ** 2 for x in range(1, 11)]
print(squares2)
