# J. Sun 2020

# Using for loop
print('\n\n')
months = ['january', 'february', 'march', 'april',
        'may', 'june', 'july', 'august', 'september',
        'october', 'november', 'december']

#create a new list----------------------
abMonths=[]
for i in range (len(months)):
    abMonths.append(months[i][0:3].title())
    print(months[i][0:3].upper(), end = '|')
print()
print(abMonths)
print(months)
