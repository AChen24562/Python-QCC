''' 1) Use a loop to print all the numbers of multiples of 3 and multiples of 7 from 3 to 77 inclusive.
2) Use a loop to print all the numbers of multiples of 3 and multiples of 7 from 77 to 3 inclusive.
Example Output
21  42  63
63  42  21'''

for x in range(3, 78):
    if x % 3 == 0 and x % 7 == 0:
        print(x, end=" ")
print()

num1 = 77
num2 = 3
while num1 >= num2:
    if num1 % 3 == 0 and num1 % 7 == 0:
        print(num1, end=" ")
    num1 -= 1
