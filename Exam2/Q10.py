'''a) Create a dictionary, people, and initialize it with the following data:
'Max': 15
'Ann': 53
'Kim': 65
'Bob': 20
'Joe': 5
'Tom': 37

b) Use a loop to print all items of the dictionary people as follows:
name is a child (if the value is younger than 12).
name is a teenager (if the value is younger than 20).
name is an adult (if the value is younger than 65).
name is a senior citizen (if the value is 65 or older).
Example Output
Max is a teenager.
Ann is an adult.
Kim is a senior citizen.
Bob is an adult.
Joe is a child.
Tom is an adult.'''

people = {
    "Max": 15,
    "Ann": 53,
    "Kim": 65,
    "Bob": 20,
    "Joe": 5,
    "Tom": 37}
for names, age in people.items():
    if age < 12:
        print(f"{names} is a child")
    elif age < 20:
        print(f"{names} is a teenager")
    elif age < 65:
        print(f"{names} is an adult")
    else:
        print(f"{names} is a senior citizen")
