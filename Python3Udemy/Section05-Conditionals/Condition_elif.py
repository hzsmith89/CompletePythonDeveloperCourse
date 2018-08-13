Grade = input("Enter your Grade: ")

if int(Grade) >= 90:
    print("Your score is A")
elif int(Grade) >= 80:
    print("Your score is B")
elif int(Grade) >= 70:
    print("Your score is C")
elif int(Grade) >= 60:
    print("Your score is D")
else:
    print("You failed :(")