courses_list = ["ET 574", "MA 771", "HIST 112"]

print(courses_list)
print(f"I have {len(courses_list)} courses")
print(courses_list[0])
print(courses_list[-1])

n = [2, 4]
print(n)
n.insert(1, 3)
print(n)
n.insert(0, 1)
print(n)
n.insert(0, 0)
print(n)
n.append(5)
print(n)

del n[0]
print(n)
value1 = n.pop(1)
print("\nRemoved %d" % value1)
print(n, "\n")

value2 = n.pop(2)
print("Remove %d" % value2)

print("Sum of the removed %d" % (value1 + value2))

newlist = n.copy()
n.clear()

print(n)
print(newlist)
