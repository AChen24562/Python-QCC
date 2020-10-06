# Tuples, cannot be deleted
n = 6, 7, 6, -2
print(n)
print(len(n), max(n), min(n))

# Tuple work
fruits = ('apple', 'banana', 'cherry')
location = fruits.index('cherry')
print(location)

a = 1, 2, 3
b = ('a', 'b', 'c')
c = a + b

t = (a, b, c)
print(t)

fruits = ('apple', 'banana', 'cherry')

print(fruits)

# Adding to a tuple
listFruits = list(fruits)
listFruits[0] = 'orange'
listFruits.append('pineapple')
tupleFruits = tuple(listFruits)
print(tupleFruits)

#  ASCII
a = 2
b = 3
print(chr(104) + chr(105))
print(ord('a') - ord('A'))
print(ord('a'), ord('A'))


let = input("Enter A, B or C: \n") let = let.upper()

if (let == 'A'):
    print('\nA, my name is Alice.')
elif (let == 'B'):
    print('\nTo be, or not to be.')
elif (let == 'C'):
    print('\nOh, say, can you see.')
else:
    print('\nInvalid letter.')
