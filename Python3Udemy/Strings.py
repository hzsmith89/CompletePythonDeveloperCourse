#from django.template.defaultfilters import upper, lower

name="Halsey Smith"

# Find number of characters in String
StrLen=len(name)
print(StrLen)

#Upper case for string but django is being a bitch
#print(upper(name))

#Lower case for string but django is being a bitch
#print(lower(name))

#String concatination
title="your grade is {}".format(79)
print(title)

str1="San Francisco"
str2=" is good"

print(str1 + str2)
print((str1 + "{}").format(str2)) #lolz