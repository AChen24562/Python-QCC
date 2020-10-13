list = ['tom', 'jerry', 'admin', 'George', 'DORA']
current_users_lower = [current_users.title() for current_users in list]


amount_of_new = int(input("Enter the amount of users: "))
new_users = []

for x in range(amount_of_new):
    new = input(f"Enter your username{x}: ")
    new_users.append(new.title())


for new in new_users:
    if new in current_users_lower:
        print(f"\nSorry {new}, that username is taken")
    else:
        print(f"\n{new} is avaialbe!!")
        list.append(new)


print(f"\nCurrent users: {list}")
