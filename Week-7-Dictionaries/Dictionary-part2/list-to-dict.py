# Ex 2
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict = dict(zip(keys, values))
print(dict)

# Ex 3, merge 2 dictionaries together
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

dict3 = dict1.copy()
dict3.update(dict2)

print(dict3)