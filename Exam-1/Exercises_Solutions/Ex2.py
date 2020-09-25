# J. Sun 2020
# using strings/lists

#A------------
strNum = '5, 10, 99, -4, 3'
print(strNum[0], strNum[-1])
print(strNum[:])
print(strNum[0] + strNum[-1])
print(len(strNum))
print(type(strNum))

#B---------
n = [5,10,99,-4,3]
print(n[0], n[-1])
print(n[:])
print(n[0] + n[-1])
print(len(n))
print(type(n))


#C------------
fruits = ['kiwi', 'pear', 'orange', 'apple', 'cherry', 'pineapple']
print(fruits.pop(3))
print(fruits)
print(fruits.remove('pear'))
print(fruits)
#print(del fruits[0])

#D ----------------
letters = 'a,b,c'
print(letters.split(','))
print('')

#E-----------------
star = 'a**b**c'
letList = star.split('**')
print(letList)
print(letList[0])
print(letList[-1])
print(letList[len(letList)//2])
print('')

#F ----------------
line1 = ['to', 'be']
line2 = ['or', 'not']
newLine = line1+line2+line1
print(newLine)
print(newLine[0])
print()

#G ----------------
line = ' '.join(newLine)
print(line)
print(line[0])
