data = [4, 5, 120, 125, 135, 155, 124, 130, 306, 107, 175, 350, 108]
min_valid = 100
max_valid = 200
Top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if min_valid > value or value > max_valid:
        print(Top_index - index, value)
        del data[Top_index - index]
print(data)
