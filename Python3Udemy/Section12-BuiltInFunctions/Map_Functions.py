list_items = [1, 2, 3, 4, 5, 6, 7]
temp_list = []

# Without Map
for item in list_items:
    temp_list.append(item ** 2)

print(temp_list)

# With Map at 2nd power
print(list(map(lambda x: x ** 2, list_items)))

# With Map at 3rd power
print(list(map(lambda x: x ** 3, list_items)))
