# Alex Chen
# Prof. Sun
# ET 574

rank = {1: 'Freshman',
        2: 'Sophmore',
        3: 'Junior',
        4: 'Senior'}

number_years = int(input("Enter the # of years you're in school: "))


if number_years in rank.keys():
    print(f"Year {number_years}: {rank.get(number_years)}")
else:
    print("Invalid year")
