# print(range(100))
# print(list(range(10)))
#
# even = list(range(0, 100, 2))
# odd = list(range(1, 100, 2))
#
# print(even)
# print(odd)

# my_string = "abcdefghijklmnopqrstuvwxyz"
# print(my_string.index('e'))
# print(my_string[4])
#
# small_decimals = range(0,10)
# print(small_decimals)
# print(small_decimals.index(3))
#
# odd = range(1,10000,2)
# print(odd)
# print(odd[985])

# sevens = range(7,1000000,7)
#
# x = int(input("Please enter a positive number less than one million: "))
#
# if x in sevens:
#     print("Number {} is divisible by seven".format(x))

# my_range = small_decimals[::2]
# print(my_range)
# print(my_range.index(4))

my_decimals = range(0, 100)
print(my_decimals)

print("=" * 40)

for i in my_decimals[3:40:3]:
    print(i)

print("=" * 40)

my_range = my_decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print("=" * 40)

for i in range(3, 40, 3):
    print(i)

print(my_range == range(3,40,3))
print(my_range == my_decimals[3:40:3])