pangram = """The quick brown
fox jumps over \t
the lazy dog"""

words = pangram.split()
for index,items in enumerate(reversed(words)):
    print(index, items)

numbers = ["2","9","5","36","456","589","636","854","748","807"]
#
# q = (numbers.split(" | "))
#
# print(q)
#
# m = " ".join(numbers)
a = []
for index in range(len(numbers)):
    numbers[index] = int(numbers[index])

print(numbers)
print(numbers[4] % 9)