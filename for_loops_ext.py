number = "9,334,597,342,673,912"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber += char

newNumber = int(cleanedNumber)
print(newNumber)

for i in range(0, 100, 5):
    print(i)

for state in ['not pin in', 'no more', 'a stiff', 'beret of life']:
    print("The parrot is " + state)

for i in range(1, 13):
    for j in range(1, 13):
        print("{0} times {1} is {2}".format(i, j, i * j))
