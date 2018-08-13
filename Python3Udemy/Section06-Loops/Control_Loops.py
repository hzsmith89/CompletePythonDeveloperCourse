word = "Python"

for letter in word:
    if letter.lower() == "t":
        continue
    print(letter)

print()

for letter in word:
    print(letter)
    if letter.lower() == "t":
        break

print()
print("App is done")
print()

ls = [1, 33, 45, 32, 55, 22, 23, 100]

for item in ls:
    if item == 55:
        print("Number found!")
        break
