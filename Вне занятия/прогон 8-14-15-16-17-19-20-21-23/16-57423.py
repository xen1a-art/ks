from sys import setrecursionlimit
def f(n):
    if n >= 2025: return n
    if n < 2025: return n + f(n + 2)
setrecursionlimit(3000)
print(f(2022) - f(2023))