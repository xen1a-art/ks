from sys import setrecursionlimit
def f(n):
    if n < 100:
        return n**2
    if n > 99 and n % 2 == 0:
        return 0.5 * f(n-1)
    if n > 99 and n % 2 == 1:
        return 2*f(n-1)

setrecursionlimit(17_000_000)
print(1000*f(16_384)/f(7777))