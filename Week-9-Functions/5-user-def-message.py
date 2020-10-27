from random import *


def message(var1, var2):
    while var2 > 0:
        print(var1)
        var2 -= 1


def main():
    text = 'QCC Ranked #1'
    n = randint(1, 10)
    print(f"Text: {text}\nn: {n}\nFunction message(text, n) will print: \n\n {message(text, n)}")


main()
