def BinominalCoefficient(n,k):
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res

def CatalanNumber(n):
    c = BinominalCoefficient(2*n, n)
    return (c//(n+1))

bound = 2**32

for i in range(30):
    cnum = CatalanNumber(i)
    if (cnum > bound):
        break
    print("C(" + str(i) + ") = " + str(cnum))
