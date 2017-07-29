list_1 = []
list_2 = list()

print("List 1: {}".format(list_1))
print("List 2: {}".format(list_2))

print(list("This string is sequenced list"))

if list_1 == list_2:
    print("Lists are equal")
else:
    print("Lists are not equal")

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# another_even = sorted(even, reverse=True)
# another_even.sort(reverse=True)
# print(another_even == even)
#
# if even == another_even:
#     print("Lists are equal")
# else:
#     print("Lists are not equal")

numbers = [even, odd]
print(numbers)

for number_set in numbers:
    print(number_set)
    for value in number_set:
        print(value)


