from sys import setrecursionlimit

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (n-1)*f(n-1)
setrecursionlimit(3000)
print((f(2024) + 2*f(2023))// f(2022))