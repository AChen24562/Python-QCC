'''1) Use a loop to request a user input from the console.
2) The loop should end when a string, 'EXAM', is entered.
Example Output
Enter anything (or enter EXAM to stop): LOOP
Enter anything (or enter EXAM to stop): forever
Enter anything (or enter EXAM to stop): [a,b,c]
Enter anything (or enter EXAM to stop): 0
Enter anything (or enter EXAM to stop): 12.34
Enter anything (or enter EXAM to stop): -99.87
Enter anything (or enter EXAM to stop): EXAM'''

choice = input("Enter anything or enter EXAM to stop: ")
while choice != 'EXAM':
    choice = input("Enter anything or enter EXAM to stop: ")
