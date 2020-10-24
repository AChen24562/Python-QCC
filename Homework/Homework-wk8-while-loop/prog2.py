# Alex Chen
# ET 574
# Prof. Sun

n1 = int(input("Enter a number n1: "))
n2 = int(input("Enter a number n2: "))

if n1 < n2:
    while n1 <= n2:
        print(n1, end=":")  # Using "end" parameter to specifiy the end line
        n1 += 1

    print()

elif n1 > n2:
    for x in range(n1, n2 - 1, -1):  # Range(start, stop, step)
        print(x, end=":")

    print()

else:
    print(f"{n1} (n1) = {n2} (n2)")  # else command only runs when they are equal
