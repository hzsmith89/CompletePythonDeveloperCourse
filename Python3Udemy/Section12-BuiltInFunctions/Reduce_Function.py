from functools import reduce

list_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum1 = 0

print(list_items)

for item in list_items:
    sum1 = sum1 + item ** 2
    print(sum1)

print("Total = {}".format(sum1))

sum2 = reduce(lambda x, y: x + y ** 2, list_items)

print("Total = {}".format(sum2))
