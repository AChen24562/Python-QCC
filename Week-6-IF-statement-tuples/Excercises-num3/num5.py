usernames = ['tom', 'jerry', 'bob', 'dora', 'admin']

for names in usernames:
    if names == 'admin':
        print(f"\nHello {names}, would you like to see a status report?")
    elif names != 'admin':
        print(f"Hello {names}, thank you for logging in again")


if not usernames:
    print("No users found")
