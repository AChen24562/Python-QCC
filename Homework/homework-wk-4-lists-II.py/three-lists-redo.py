# List compreshension

fours = [n*4 for n in range(0, 11)]
print(fours)
print("")

twos = []
for n in fours:
    twos.append(n//2)

print(twos)
print("")

ones = twos[:]  # Slicing
for n in range(0, 11):
    ones[n] = ones[n]//2

print(ones)
print("")
