parrot = 'Norwegian Blue'
print(parrot)
print(parrot * 5)
# prints 4th character in the string
print(parrot[3])
# prints last character in the string
print(parrot[-1])
# prints list(array) of characters in the string ranging from 4th to the last string character
print(parrot[3:-1])

# prints until first 6 characters of the string
print(parrot[:6])
# begins with 7th character to the end of the string
print(parrot[6:])

# slices the string from ending characters
print(parrot[-6:-2])

# slices the string's characters by using steps of 2
print(parrot[0:6:2])
print(parrot[0::2])

print("Blue" in parrot)
