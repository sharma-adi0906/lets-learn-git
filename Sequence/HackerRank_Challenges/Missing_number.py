def missing_number(test, array, n):
    for i in range(1, n):
        if test[i] == array[i]:
            return True


n = int(input())
A = []
self = []
i = 1
j = 1
m = 1
while i < n:
    A.append(i)
    i += 1

while len(self) < n:
    j = int(input())
    self.append(j)
while m <= n:
    if missing_number(self, A, n) is True:
        pass
        m += 1
    else:
        print(self)
        m += 1
