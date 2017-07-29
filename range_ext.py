decimal = range(0, 100)
my_range = decimal[3:40:3]

print(list(decimal))
print(list(my_range))

print(list(range(0, 100)[3:40:3]))

print(list(range(0, 5, 2)) == list(range(0, 6, 2)))
print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))

print("=" * 50)

r = range(0, 100)

for i in r[::-2]:
    print(i)

print("=" * 50)

for i in range(99, 0, -2):
    print(i)

print("=" * 50)

# This loop won't execute because range is incorrect,
# correct order is as in previous example above

for i in range(0, 99, -2):
    print(i)

print("=" * 50)

print(range(0, 100)[::-2] == range(99, 0, -2))
print(list(range(0, 100)[::-2]))
print(list(range(99, 0, -2)))

print("=" * 50)

backward_string = 'egaugnal lufrewop a si nohtyP'
print(backward_string[::-1])

# mini challenge

o = range(0, 100, 4)
print(list(o))
p = o[::5]
print(p)

for i in p:
    print(i)
