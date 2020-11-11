# Alex Chen
# ET 574 - Project #2
# Prof. Sun


def info():
    item = input("Enter name of item: ")
    year = int(input("Enter year purchased: "))
    cost = int(input("Enter cost of item: "))
    life = int(input("Enter life of item <years>: "))
    method = input("Enter method of depreciate <SL or DDB>: ")
    print(f'''\nDescription: {item.title()}
    Year of purchase: {year}
    Cost: ${cost}
    Estimated Life: {life}
    Method of depreciation: {method} ''')


def main():
    info()


main()
