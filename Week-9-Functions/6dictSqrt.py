from math import *


def dictSqrt(num):
    list = []
    for x in range(0, num):
        list.append(x)
    sqrtNum(list)


def sqrtNum(list1):
    list2 = []
    for x in list1:
        squares = isqrt(x)
        list2.append(squares)
    print(dict(zip(list1, list2)))


dictSqrt(3)
