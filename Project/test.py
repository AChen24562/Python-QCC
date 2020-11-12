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


depreciation_SL(2016, 2000, 5)
