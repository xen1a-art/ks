from sys import setrecursionlimit
def f(n):
    if n < 5:
        return n
    if n >= 5:
        return 2*n*f(n-4)
setrecursionlimit(14_000)
print((f(13_766)- 9*f(13_762))/f(13_758))