# Original list of users
list = ['tom', 'jerry', 'admin', 'George', 'DORA']

# List of original users, but changed so that it can be case-sensitive
current_users = [old_users.title() for old_users in list]

# Input amount of users
amount_of_new = int(input("Enter the number of users: "))

# New list for new users
new_users = []

# Run this loop up to as many times requested
# Request name evertime it loops and append it to the new user list with first letter capilized
for x in range(1, amount_of_new + 1):
    new = input(f"Enter your username{x}: ")
    new_users.append(new.title())

# Run through both new user list and original users list
# If new user matches an old user decline
# If new user doesn't match old user, accept and append to old user list
for new in new_users:
    if new in current_users:
        print(f"\nSorry {new}, that username is taken")
    else:
        print(f"\nGreat {new} is avaialbe")
        current_users.append(new)


print(current_users)
