# tuple_1 = "Sonata Arctica", "Ecliptica", 2001
# tuple_2 = ("Sonata Arctica", "Silence", 2003)

# print(tuple_2)
# print(tuple_1)

# tuple unpacking
# artist, album, release_date = tuple_1
#
# print(artist)
# print(album)
# print(release_date)

#  print(artist, album, release_date)

# x, y = 12, 3
# print("x is: {}".format(x))
# print("y is: {}".format(y))
# print(x, y)
#
# x, y = y, x
# print("x is now: {}, y is now: {}".format(x, y))

tuple_1 = "Sonata Arctica", "Ecliptica", 2001

# A tuple is a sequence of immutable Python objects.
# Tuples are sequences, just like lists.
# The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses,
# whereas lists use square brackets.

tuple_2 = tuple_1[0], tuple_1[1], tuple_1[2], ((1, "8th commandmant"), (2, "Full Moon"))
print(tuple_2)

print("=" * 45)

artist, album, release, tracks = tuple_2
print(artist)
print(album)
print(release)
print(tracks)

print("=" * 45)
for number, song_name in tracks:
    print("No.{0} \t {1}".format(number, song_name))

