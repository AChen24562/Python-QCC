import random


def main():
    n = []
    for x in range(0, 5):
        random_num = random.randint(1, 100)
        n.append(random_num)
    print(f"Original List: {n}")
    drop_lowest(n)


def drop_lowest(n):
    n.remove(min(n))
    print(f"Removed Lowest Value: {n}")


main()
print()

n = [10, 44, 8, 78, 60]
print(f"Original Example list: {n}")
drop_lowest(n)
