# Alex Chen
# Prof. Sun
# Prog 1

from random import randint


def isInRange(x):
    return x in range(-100, 100)


def main():
    for x in range(10):
        n = randint(-500, 500)
        if isInRange(n):
            print(f"{n} is in the range")
        else:
            print(f"{n} in NOT in range")


main()
