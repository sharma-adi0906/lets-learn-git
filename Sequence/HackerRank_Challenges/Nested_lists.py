# Name = []
# Age = []
# n = int(input("enter number of students? "))
#
# for i in range(0, n):
#     x = input()
#     Name.append(x)
#     j = 1
#     while j != 2:
#         y = int(input())
#         Age.append(int(y))
#         Name.append(Age)
#         j += 1
#     i += 1
# print(Name)

Name = []
Age = []
n = int(input("enter number of students? "))
for i in range(1,(n*2) + 1):
    m = input()
    if m.isnumeric():
        Age.append(int(m))
    else:
        Name.append(m)
    i += 1

for index,items in enumerate(Age):
    print(index, Age)


n = min(Age)
s = Age.index(n)
print(Name[s])