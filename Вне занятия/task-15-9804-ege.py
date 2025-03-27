def dell(n,m):
    return m&n

def f(a):
    for x in range(1,10_000):
        f = (x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))
        if not f:
            return False
    return True

for a in range(1,10_000):
    if f(a):
        print(a)
        break