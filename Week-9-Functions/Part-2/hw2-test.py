from random import randint


def isInRange(x):
    return x in range(-100, 100)


def main():
    for x in range(10):
        n = randint(-500, 500)
        if isInRange(n):
            print(f"{n} ok")
        else:
            print(f"{n} no ")


main()
