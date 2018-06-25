ages=[22,3,44,50,90,1] # mutable - it cannot change
print(ages)
print("Append element to list")
ages.append(100)
print(ages) # print all elements in tuple
print(ages[1:3]) # prints second and third elements
ages.insert(1,55)
print(ages)

print("Sentence Splitting")
str="Welcome to the Black Parade"
words=str.split(" ")
print(words)
print(words[0:3])