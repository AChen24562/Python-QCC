# Alex Chen
# ET 574 - Project #2
# Prof. Sun


def info(item, year, cost, life, method):

    print(f'''\nDescription: {item.title()}
    Year of purchase: {year}
    Cost: ${cost}
    Estimated Life: {life}
    Method of depreciation: {method} \n''')

    if method == "Straight-Line":
        depreciation_SL(year, cost, life)
    elif method == "Double Declining Balance":
        depreciation_DDB(year, cost, life)
    else:
        print("Incorrect choice for method")


def depreciation_SL(year, cost, life):
    print(f"\t{'Value At Beg. of Yr.' : <20}{'Amount Depre During Year': ^35}{'Total Deprec to End of Year': >20}")

    counter_total_dep = 0
    adjusted_cost = cost
    for x in range(1, life + 1):
        depreciation_value = (1 / life) * cost
        counter_total_dep += depreciation_value
        print(f"{year}\t{adjusted_cost: <20}{depreciation_value: >28}{counter_total_dep: >33}")
        adjusted_cost -= depreciation_value
        year += 1


def depreciation_DDB(year, cost, life):
    print(f"\t{'Value At Beg. of Yr.' : <20}{'Amount Depre During Year': ^35}{'Total Deprec to End of Year': >20}")

    counter_total_dep = 0
    adjusted_cost = cost
    for x in range(1, life+1):
        depreciation_value = (2/life) * adjusted_cost
        counter_total_dep += depreciation_value
        if x == life:
            depreciation_value = adjusted_cost
            counter_total_dep = cost
            print(f"{year}\t{adjusted_cost: <20}{depreciation_value: >28}{counter_total_dep: >33}")
            break
        print(f"{year}\t{adjusted_cost: <20}{depreciation_value: >28}{counter_total_dep: >33}")
        adjusted_cost -= depreciation_value
        year += 1


def main():
    item = input("Enter name of item: ")
    year = int(input("Enter year purchased: "))
    cost = eval(input("Enter cost of item: "))
    life = int(input("Enter life of item <years>: "))
    method = input("Enter method of depreciate <SL or DDB>: ")

    if method.upper() == 'SL':
        method = "Straight-Line"
    elif method.upper() == 'DDB':
        method = "Double Declining Balance"
    info(item, year, cost, life, method)


main()
