age = 24
# convert number into string with str()
print("My age is: " + str(age) + " years")

# outputting data format with place fields - supported in python 3
# placement fields can be repeated and used as unordered
print("My age is: {0} years".format(age))
print("{1} is the {0}st month in each year".format(1, "January"))

# right(default) formated output with 4 spaces allocated
for i in range(1, 12):
    print("No {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# left formated output with 4 spaces allocated
for i in range(1, 12):
    print("No {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print("PI is aproximately {0:12.50f}".format(22 / 7))

# implicit placement fields show data in order
for i in range(1, 12):
    print("No.{} squared is {:4} and cubed is {:4}".format(i, i ** 2, i ** 3))


# outputting data format with string operators - supported in python 2
# string operators can't be repeated and must be used in written order
print("My age is %d" % age)
print("My age is %d %s and %d %s" % (age, "years", 6, "months"))

for i in range(1, 12):
    print("No %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))

print("PI is aproximately %12.50f" %(22 / 7))