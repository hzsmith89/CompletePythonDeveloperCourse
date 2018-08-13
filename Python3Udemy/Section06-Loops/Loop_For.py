for i in range(10):
    print(i);

ls = [1, 2, 3, "hi", 55, 92]

print()

for i in range(6):
    print("index[{}]={} {}".format(i, ls[i], type(ls[i])))

print()

for i in ls:
    print(i)
