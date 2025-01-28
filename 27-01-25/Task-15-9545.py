def dell(x,d):
    return x % d == 0
def f(A):
    for x in range(0, 1000):
        f = (dell(x, 10) and dell(x, 26) and (x >= 300)) <= (A <= x)
        if not f:
            return False
    return True

for A in range(0, 10_000)[::-1]:
    if f(A):
        print(A)
