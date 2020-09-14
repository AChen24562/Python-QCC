# Alex Chen
# Prof. Sun
# List Homework

mygrades = [92, 51, 83, 37, 72]

print(mygrades)
print(f"Average: {sum(mygrades) / len(mygrades):.2f}")

median_index = len(mygrades) // 2
print(f"Median: {mygrades[median_index]}")

# For median of an ordered set:
    #  import statistics as st
    #  print(st.median(mygrades))

# More efficient for longer data sets:
# for grade in mygrades:
    # if grade < 60:
        # mygrades.remove(grade)

mygrades.remove(51)
mygrades.remove(37)
print()
print(mygrades)
