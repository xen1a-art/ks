from sys import setrecursionlimit
def f(n):
    if n < 110:
        return n
    if n >= 110:
        return n + f(n-1)
setrecursionlimit(3000)
print(f(2025)-f(2021))