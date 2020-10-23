n = 1
while n < 101:
    if n % 2 == 0:
        print(n)
    n += 1

print()
n = 1
while n <= 100:
    if n % 2 == 0 and n % 5 == 0:
        print(n)
    n += 1

print()

# 9 - 0 While loop
n = 9
while n >= 1:
    print(n)
    if n == 1:
        print("Happy New year")
    n -= 1
print()
# 9 - 0 For Loop
for x in range(9, 0, -1):
    print(x)
