my_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

my_iterator = iter(my_list)

for item in range(0, len(my_list)):
    print(next(my_iterator))

for i in my_list:
    print(i)
