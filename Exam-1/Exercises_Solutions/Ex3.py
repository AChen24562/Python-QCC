# j. sun 2020
#Review list methods

#a) Use a for loop to ask the user to enter five floating point grades.
#b) Use append () method to add each grade to an empty list, grades in the loop.
print('\n\n')
grades = []
i = 1
for n in range(3):
    n = float(input(f"Enter a grade {i} : "))
    grades.append(n)
    i+=1
print(f'\nOriginal list: \n{grades}')

#c) Use sorted () method to print sorted the list.
print(f'\nSorted list:\n{sorted(grades)}\n')

#d) Use the max () method to print the highest grade in the list.
print('Max =', max(grades),'\n')

#e) Use the min () method to print the lowest grade in the list.
print('Min =', min(grades),'\n')

#f) Use the sum () method to print the total of all the grades in the list.
print('Sum =', sum(grades),'\n')

#g) Use the len () method to print the number grades in the list.
print('Length of List =', len(grades),'\n')

#h) Compute and print the average with two decimal places.
print(f'Average = {sum(grades)//len(grades):.0f}')

#i) Append the average to the end of the list.
grades.append(round(sum(grades)//len(grades)))

#j) Use input () to request user’s name.
name = input('\nEnter your name: ')

#k) Use insert () method add user’s name to the first item in the list.
grades.insert(0, name)

#l) Use input () to request user’s id.
id= input('\nEnter your id: ')

#m) Use insert () method add user’s id to the second item
#in the list with ‘574’ as a prefix.
#prefix = '574'
grades.insert(1, '574'+id)

#n) Display the list, grades and type of the list,
print(f'\nFinal list:\n{grades}\n\nList type:{type(grades)}')

print("")
