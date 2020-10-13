NY = {"BX": 1.42,
      "MN": 1.63,
      "QS": 2.25,
      "BN": 2.56,
      "SI": 0.47}


NY.update({"NU": 1.34})
print(NY)

NY["SK"] = 1.49
print(NY)

for x in NY.values():
    if x > 2.5:
        print("Brooklyn is Kings county")

newYork = dict(NY)
del newYork["BN"]
print(len(NY))
print(len(newYork))
