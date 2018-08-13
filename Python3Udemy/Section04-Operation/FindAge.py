import datetime
DOB=input("Enter your DOB: ")
CurrentYear=datetime.datetime.now().year
Age = CurrentYear-int(DOB)
if (Age >= 18):
    print("Your age is {}".format(Age))
elif (Age >= 16):
    print("You can at least drive.")
else:
    print("You're a baby...")

for x in range(Age):
    print(x)