NY = {"BX": 1.42,
      "MN": 1.63,
      "QS": 2.25,
      "BN": 2.56,
      "SI": 0.47}

print(NY['QS'])
print(NY.get("QS"))

print(NY.get("LI", "Not avaialbe"))

# True/False statements
print("LI" in NY)
print('MN' not in NY)

# Print alphabetical min max
print(len(NY), min(NY), max(NY))

# Print numerical min max
print(len(NY.items()), max(NY.keys()), min(NY.values()))

print()
# QS = 2.25
print(round(NY['QS']))
NY['QS'] += .3
print(round(NY['QS']))


for x in sorted(NY, reverse=True):
    print(x, end='|')
print()

for x in sorted(NY.values(), reverse=True):
    print(x, end=', ')
