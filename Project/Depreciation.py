# Alex Chen
# ET 574 - Project #2
# Prof. Sun


def info():
    item = input("Enter name of item: ")
    year = int(input("Enter year purchased: "))
    cost = int(input("Enter cost of item: "))
    life = int(input("Enter life of item <years>: "))
    method = input("Enter method of depreciate <SL or DDB>: ")

    if method.upper() == 'SL':
        method = "Straight-Line"
    elif method.upper() == 'DDB':
        method = "Double Declining Balance"

    print(f'''\nDescription: {item.title()}
    Year of purchase: {year}
    Cost: ${cost}
    Estimated Life: {life}
    Method of depreciation: {method} \n''')

    if method == "Straight-Line":
        depreciation_SL(year, cost, life)


def depreciation_SL(year, cost, life):
    print("\tValue At Beg. of Yr.".ljust(40),end="")
    print("\tAmount Depre During Year".center(40),end="")
    print()
    counter_total_dep = 0
    adjusted_cost = cost
    for x in range(1, life + 1):
        depreciation_value = (1 / life) * cost
        counter_total_dep += depreciation_value
        print(f"{year}\t{adjusted_cost:.2f}\t{depreciation_value:.2f}\t{counter_total_dep:.2f}")
        adjusted_cost -= depreciation_value


def main():
    info()


main()
