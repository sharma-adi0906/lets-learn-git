Pangram = "The quick brown fox jumps over the lazy dog"
letter = sorted(Pangram)
print(letter)

numbers = [2.3, 4.6, 8.6, 14.6, 3.4, 8.9, 45.2, 77.25]
sort_it = sorted(numbers)
print(sort_it)

missing_letters = sorted("The quick brown fox jumps on a lazy dog",
                         key = str.casefold)
print(missing_letters)

a = list("546785256466")

print(a)
b = str(a)
print(b)
print(id(a))
print(id(b))

c = sorted(b)
print(c)

print(c is a)