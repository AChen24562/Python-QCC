# Alex Chen
# Prof. Sun
# ET 574

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july'
          , 'august', 'september', 'october', 'november', 'december']


# New list with 3-letter abbreviation
three_letter = []
for x in months:
    three_letter.append(x[:3])


# Method of  printing list seperated by '|'
for x in three_letter:
    print(x.upper(), end = "|")
print()

# Another method of printing list seperated by '|'
"""
print()
print('|' .join(three_letter)) """

# Print 3-letter list
for i in range(len(three_letter)):
    three_letter[i] = three_letter[i].title()
print(three_letter)
# Print original list
print(months)
