''' Translate the following for loop to the equivalent while loop.

for n in range (100, 600, 100)
    print(n)


Make sure to precisely match the output below.

100
200
300
400
500'''

num1 = 100
while num1 < 600:
    print(num1)
    num1 += 100
