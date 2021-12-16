letters = "abcdefghijklmnopqrstuvwxyz"

backwards = (letters[25::-1])   #or we say print(letters[::-1]) that means the same,
                                # so if we see a -1 at the place of step we understand it as reverse of the string

print(backwards)

print(letters[16:13:-1])   #to print qpo
print(backwards[21::1])     #to print edcba
print(backwards[:8:1])  #last 8 characters of string backwards
