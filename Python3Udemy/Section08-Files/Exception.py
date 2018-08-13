
def main():

    try:
        x = int(input("Enter number: "))
        print(x+5)
    except ValueError:
        print("You need to enter a number!")


if __name__ == '__main__':
    main()
