# Inserting lists within tuples gives possibility to implement both immutable(for tupels),
# and mutable(for lists that hold tuples) features
# In this example below immutable part represents permanent tuple data sequence, while
# expandable data sequence is the tuple sequence encompassed within list.
# List within tuple can expand "tracks" tuple sequence.

imelda = "More Mayhem", "Imelda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])

print(imelda)

# Expanding list sequence with tuple that belongs to tuple "imelda"
imelda[3].append((5, "All For You"))

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)

# Expanding list sequence with tuple that belongs to tuple "imelda"
tracks.append((6, "Eternity"))
print(tracks)

# unpacking "songs" tuple in "track" list
for songs in tracks:
    # unpacking "songs" tuple
    track, title = songs
    print("\tTrack number {}, Title: {}".format(track, title))