a = []
n = int(input("enter the number of digits to be operated?\t"))
for i in range(0, n):
    k = int(input())
    a.append(k)
print("for sum write +, for subtraction write -, for multiplication write X and then press enter")
m = input()
if m == "+":
    c = sum(a)
elif m == "-":
    for i in range(0, n):
        if a[i] > a[i+1]:
            c = a[i] - a[i+1]
        else:
            c = a[i+1] - a[i]
elif m == "X":
    for t in range(0, n):
        c = a[i] * a[1+1]
        i += 1
print(c)
