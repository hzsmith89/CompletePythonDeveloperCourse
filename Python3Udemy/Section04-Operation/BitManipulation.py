x = 0b10101
y = 0b01101
print(x)
print(y)


def f(n):
    print('{:08b}'.format(n) + ' = ' + str(n))

f(x)
f(y)
f(x&y)
f(x|y)
f(x>>2)
f(y<<3)
