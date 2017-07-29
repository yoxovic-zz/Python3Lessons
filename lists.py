# ip_adress = input("Please enter your IP adress:")
# print(ip_adress.count("."))

parrot = ["non pinin", "no more", "a stiff", "bereft of live"]

parrot.append("Norwegian Blue")

for state in parrot:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

number_list = even + odd
# number_list.sort()
sorted_list = sorted(number_list)
# print(number_list)
print(sorted_list)

if number_list == sorted_list:
    print("lists are equal")
else:
    print("lists are not equal")

if sorted(number_list) == sorted_list:
    print("lists are equal")
else:
    print("lists are not equal")
