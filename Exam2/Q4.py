'''1) Request a user input for the variable, direction.
2) Write an if-elif-else statement to do the following:
    a) if the direction is 'N', print a message, North Zone.
    b) if the direction is 'S', print a message, South Zone.
    c) if the direction is 'E', print a message, East Zone.
    d) if the direction is 'W', print a message, West Zone.
    e) if the direction is none of the above, print a message, Invalid Input.
    f) uppercase and lowercase should be all acceptable.
Example Output 1
Enter your direction(N/S/E/W): uptown
Invalid Input.


Example Output 2
Enter your direction(N/S/E/W): e
East Zone.'''
direction = input("Enter a direction (N/S/E/W): ")
direction = direction.title()
if direction == 'N':
    print("North Zone")
elif direction == 'S':
    print("South Zone")
elif direction == 'E':
    print("East Zone")
elif direction == 'W':
    print("West Zone")
else:
    print("Invalid Input")
