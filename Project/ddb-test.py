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
            print(f"{year}\t{adjusted_cost: <20,.2f}{depreciation_value: >28,.2f}{counter_total_dep: >33,.2f}")
            break
        print(f"{year}\t{adjusted_cost: <20,.2f}{depreciation_value: >28,.2f}{counter_total_dep: >33,.2f}")
        adjusted_cost -= depreciation_value
        year += 1



depreciation_DDB(2016, 2000, 5)
