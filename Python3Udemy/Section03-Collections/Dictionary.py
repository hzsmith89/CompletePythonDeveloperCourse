person = dict(Name="Halsey", Age=29, Salary=100000)
print(person)
print(person["Name"])
print(person["Age"])
print(person["Salary"])

print("Updating Name")
person["Name"] = "Zachary"
print(person["Name"])

print("Adding Insurance")
person["Insurance"] = True
print(person)

print("Checking if insured")
if person["Insurance"]:
    print("You're covered!")
else:
    print("Get out of here loser!")

print("Deleting Age")
del person["Age"]
print(person)

print(person["Salary"])