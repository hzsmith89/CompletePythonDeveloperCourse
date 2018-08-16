list_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temp_list = []

# Without Filter
for item in list_items:
    if item % 2 == 0:
        temp_list.append(item)

print(temp_list)
print(*temp_list, sep=":")

# With Filter
print(*filter(lambda x: x % 2 == 0, list_items), sep=", ")

print(*range(10), sep="-")
