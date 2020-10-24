dict1 = {}

keys = []
uppercase_keys = []
values = []
x100values = []
letter = 97

for x in range(26):
    keys.append(chr(letter))
    uppercase_keys.append(chr(letter).upper())
    letter += 1

for x in range(1, 26 + 1):
    values.append(x)
    x100values.append(x * 100)

charNum24 = dict(zip(keys, values))
CharNum24 = dict(zip(uppercase_keys, x100values))
print(charNum24)
print(CharNum24)
