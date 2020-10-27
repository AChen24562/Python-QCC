current_users = ['bill', 'jerry', 'jeff', 'albert', 'alfred']

current_users_lower = [user.lower() for user in current_users]

print(f"current users: {current_users}\n")
new_user = input("Enter a username: ")

if new_user.lower() in current_users_lower:
    print(f"{new_user} is taken")
else:
    print(f"{new_user} is available")
