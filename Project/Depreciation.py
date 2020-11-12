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
    Method of depreciation: {method} ''')

    if method == "Straight-Line":
        depreciation_SL(year, cost, life)


def depreciation_SL(year, cost, life):
    print("\tValue At Beg. of Yr.\tAmount Deprec During Year\tTotal Deprec to End of year")


def main():
    info()


main()
