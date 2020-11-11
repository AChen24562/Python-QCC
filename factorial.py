num = 12312

factorial = 1

while num > 1:
    factorial *= num
    num -= 1

print(factorial)


def iterative(num, factorial):
    if num == 1:
        print(factorial)
    else:
        factorial *= num
        num -= 1
        iterative(num, factorial)


factorial = 1
iterative(12, factorial)
