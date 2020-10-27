'''Use a loop to print all the odd numbers from 100 to 90  inclusive.
When the number is 99, just skip it and jump directly to the next iteration in the loop.


Make sure to precisely match the output below.

97
95
93
91 '''
x = 100

while x > 90:
    if x == 99:
        x -= 1
        continue
    elif x % 2 == 1:
        print(x)
    x -= 1
