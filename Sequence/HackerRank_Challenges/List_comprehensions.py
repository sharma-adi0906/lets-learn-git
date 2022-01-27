x = int(input()) + 1
y = int(input()) + 1
z = int(input()) + 1
n = int(input())
permutations = []
i = j = k = 0
for i in range(0, x):
    for j in range(0, y):
        for k in range(0, z):
            p = i+j+k
            if p != n:
                m = [i,j,k]
                permutations.append(m)


print(permutations)