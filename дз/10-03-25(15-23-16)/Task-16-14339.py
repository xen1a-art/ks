from sys import setrecursionlimit
def f(n):
    if n < 11:
        return n
    if n >= 11 and n % 2 == 0:
        return 2*n-3+f(n-2)
    return 3*n-4+f(n-3)

setrecursionlimit(6000)
print(f(5500)-f(5497))
