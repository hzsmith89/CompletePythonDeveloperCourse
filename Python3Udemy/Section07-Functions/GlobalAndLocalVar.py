x = 10


def show():
    global x
    print(x)


def main():
    global x
    print("x={}".format(x))
    show()


if __name__ == '__main__':
    main()
