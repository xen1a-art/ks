from sys import setrecursionlimit

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2*n*f(n-1)
setrecursionlimit(4000)
print((f(2024)//16-f(2023))/f(2022))