data = [104, 107, 4, 105, 103, 5, 107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200
for index in range(len(data) - 1, -1, -1):
    print(index, data[index])
    print()
    if data[index] < min_valid or data[index] > max_valid:
        print(index, data)
        del data[index]
print(data)