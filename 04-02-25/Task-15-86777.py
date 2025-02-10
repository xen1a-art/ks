def dell(n,m):
    return n % m == 0

def f(A):
    for x in range(1,10_000):
        for B in range(80,100):
            f = dell(x,17) <= ((not B) or (A < x + 30))
            if not f:
                return False
    return True

for A in range(1,10_000)[::-1]:
    if f(A):
        print(A)
        break