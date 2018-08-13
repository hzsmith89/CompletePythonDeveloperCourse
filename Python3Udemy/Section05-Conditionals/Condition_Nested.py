Age = input("Enter you age: ")

if int(Age) > 18:
    print("Welcome! You are eligible")
    if int(Age) < 30:
        print("Your class is A")
    else:
        print("Your class is B")
else:
    print("I'm sorry. You're not eligible for this class.")
