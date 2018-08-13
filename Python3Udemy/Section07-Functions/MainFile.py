import datetime


def main():

    # main code function
    dob = input("Enter your DOB: ")
    current_year = datetime.datetime.now().year
    age = current_year - int(dob)
    print("Your age is {}.".format(age))


if __name__ == '__main__':
    main()
