A = []
n = int(input())
if n not in range(2, 10):
    print("Invalid Input")
else:
    A = map(int, input().split())
M = []
for items in A:
    M.append(items)
m = max(M)
M.remove(m)
n = max(M)
while n == m:
    M.remove(n)
    n = max(M)

print(max(M))
#
# A = map(int, input().split())
# print(A)