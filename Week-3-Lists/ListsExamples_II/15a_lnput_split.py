# J. Sun 2020
# using build-in input() function

'''In case Atom/F5 not working, you can always run in script mode
# how to run the command line environment
# windows
# start -> run -> type cmd
# Mac
# applications -> utilities -> terminal
'''

print('')
# request input from the console and store into a variable
name = input("Enter your name: ")
print('Hi '+name+'!')
#print(f'Hi {name}!')


#The split() method splits the string into substrings
#if it finds instances of the separator.
#split () method turns a single string into a list of substrings
fullName = name.split()
print(f'{fullName[0]}\t{fullName[1]}')
print(f'{fullName[1]}\t{fullName[0]}')
print('')

print("{}\t{}".format(fullName[0], fullName[1]))
print("{}\t{}".format(fullName[1], fullName[0]))
print('')
