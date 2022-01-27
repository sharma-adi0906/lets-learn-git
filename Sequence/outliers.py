# Testings also done for different cases of outlying values

# data = [4, 5, 120, 125, 135, 155, 124, 130, 175, 350, 360]
# data = [120, 125, 135, 155, 124, 130, 175, 350, 360]
# data = [4, 5, 120, 125, 135, 155, 124, 130, 175]
# data = [120, 125, 135, 155, 124, 130, 175]
data = []


# del data[:2]
# print(data)
#
# del data[7:]
# print(data)
print(data)
max_valid = 200
min_valid = 100

# for index, value in enumerate(data):
#     if (value < min_value) and (value > max_value):
#         del data[index]
#
# print(data)

#
#
#Above code will not work because index value will change after first iteration
#
#

# |Below we are processing the low values in data

stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)
del data[:stop]
print(data)

# process the high value in the list

start = 0
for index in range(len(data) -1, -1, -1):
    if data[index] <= max_valid:
        start = index
        break

print(start)
del data[start:]
print(data)