fruits = {
        'Apple': 1.59,
        'Pear': 1.29,
        'Kiwi': 1.69,
        'Cherry': 2.99
}

for x in sorted(fruits, reverse=True):
    print(x, end=' ')

print()

counter = 0
higher_cost = 0
for x in fruits.values():
    if x > higher_cost:
        higher_cost = x
    counter += 1
print(f"Items: {counter}\nMost Expensive: ${higher_cost}")

print()

# Less elegant method
print(f"Items: {len(fruits.items())}")
print(f"Most Expensive: {max(fruits.values())}")
