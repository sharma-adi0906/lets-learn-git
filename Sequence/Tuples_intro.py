# t = ("a", "b", "c")
# print(t)
#
# metallica = "Ride the nightstorm", "metallica", 1996
# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# # metallica[2] = 1984           Not working because cant assign in a tuple
#
# metallica2 = list(metallica)
# print(metallica2)
#
# metallica2[2] = 1986
# print(metallica2)
#

albums = [("welcome to my nightmare", "Alice cooper", 1975),
          ("Bad company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1987),
          ("More Mayhem", "Emilda", 1981),
          ("Ride the lightening", "Metallica", 1984)]

for song, artist, year in albums:
    print("song= {0}, artist= {1}, year= {2}".format(song,artist,year))









