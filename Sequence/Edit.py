arr = list()
sub_A = list()
sub_B = list()
happiness = 0
n = int(input())
m = int(input())

for i in range(0, n):
    p = input(int())

    arr.append(p)

    i += 1
for i in range(0, m):
    q = input(int())

    sub_A.append(q)

    i += 1

for k in range(0, m):

    r = input(int())

    sub_B.append(r)

    k += 1

for i in range(0, n):
    if arr[i] in sub_A:
        happiness += 1
    if arr[i] in sub_B:
        happiness -= 1

print(happiness)
