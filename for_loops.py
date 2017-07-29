# for i in range(20):
#     print("i is now {}".format(i))
#
# for i in range(1,20):
#     print("i is now {}".format(i))

# number = "9,334,597,342,673,901"
# for i in range(len(number)):
#     print(number[i])

# number = "9,334,597,342,673,901"
# for i in range(len(number)):
#     if number[i] in '0123456789':
#         print(number[i], end="")

number = "9,334,597,342,673,902"
cleanedNumber =''

for i in range(len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]

print(cleanedNumber)
newNumber = int(cleanedNumber)
print("New number is {}".format(newNumber))