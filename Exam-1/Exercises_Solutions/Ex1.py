# J.Sun
# Ex1 - traceFormat

#-------A------
print('012345678901234567890')
print('A'.rjust(5), 'B'.center(5), 'C'.ljust(5))
print()

#-------B------
print('01234567890123456')
print("{0:^7}{1:4}{2:>6s}".format('one', 'two', 'three'))
print(f"{'one':^7}{'two':4}{'three':>6s}")
print()

#-------C------
n=1234
print('01234567890123456789')
print(f"{n:10}{n:^10}")
print(f"{n:<10}{n:>10}")
print(f"{n:10.3f}{n:.2f}")
print(f"{n:10.2%}{n:20,.2%}")
print()

#-------D---------------------
q1= '''"If {0:s} dream it, {0:s} do it. - Walt Disney"'''
print(q1.format('you can'))

a = 'ONE'
b = 'DAY'
q2 = f"\"{a} {b} or {b} {a}. You decide. Paulo Coelho\""
print(q2)
q2 = "\"{0} {1} or {1} {0}. You decide. Paulo Coelho\""
print(q2.format(a,b))

print()
