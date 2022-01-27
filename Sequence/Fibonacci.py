# i1 = 0
# i2 = 1
# m = 0
# k = 0
# j = int(input("Enter the last digit of series? "))
# print("{0}\n{1}".format(i1, i2))
# while k < j:
#     k = i1 + i2
#     i1 = i2
#     i2 = k
#     if k < j:
#         print(i2)


def fibonacci(n):
    """Return the n th number for positive `n`"""
    if 0 <= n <= 1:
        return n

    n_minus2, n_minus1 = 0, 1
    result = None
    for f in range(n - 1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result
    return result


k = int(input("Enter the range? "))
for p in range(k):
    print(p, fibonacci(p))
