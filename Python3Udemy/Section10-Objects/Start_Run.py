from Class_OP import MultiOperations

def main():
    ops = MultiOperations()
    x = 3
    y = 4
    print("{} plus {} == {}".format(x, y, ops.sum(x, y)))
    print("{} minus {} == {}".format(x, y, ops.sub(x, y)))
    print("{} times {} == {}".format(x, y, ops.mult(x, y)))
    print("{} divided by {} == {}".format(x, y, ops.div(x, y)))


if __name__ == '__main__':
    main()


