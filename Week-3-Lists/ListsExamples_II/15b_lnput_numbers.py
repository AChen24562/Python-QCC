# J. Sun 2020
# using build-in input() function

print('')
# request input from the console and store into a variable
prompt = "Enter an integer: "
# type casts/returns an integer number
n = int(input(prompt))
# display the result
print (f'n+1 = {n+1}')
print ('n+1 = '+str(n+1))
print('')

# request input from the console and store into a variable
prompt = "Enter a float: "
# type casts/returns a floating point number
m = float(input(prompt))
# display the result
print (f'm*100= {m*100:.2f}')
print ('m*100 = '+str(m*100))
print('')

# request input from the console and store into a variable
prompt = "Enter a number: "
# The eval() function evaluates the specified expression,
# if the expression is a legal Python statement, it will be executed.
a = eval(input(prompt))
# display the result
print (f'{a}')
print('')
