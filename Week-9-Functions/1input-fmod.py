from math import *

num1 = int(input("Enter a numerator: "))
deno1 = int(input("Enter a denominator: "))

print(f"{num1} mod {deno1} = {fmod(num1, deno1):.0f}")
