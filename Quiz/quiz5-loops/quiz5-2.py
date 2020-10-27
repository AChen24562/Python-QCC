'''Use a while loop to horizontally print all the odd numbers from -9 to 9 inclusive.
Make sure to use ' | ' to precisely match the output format below.


Example Output

-9 | -7 | -5 | -3 | -1 | 1 | 3 | 5 | 7  | 9 |'''
num = -9
while num <= 9:
    if num % 2 == 1:
        print(num, end="|")
    num += 1
