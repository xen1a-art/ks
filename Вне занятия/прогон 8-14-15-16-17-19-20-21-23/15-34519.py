def dell(m,n):
    return m & n

def f(A):
    for x in range(1,10_000):
        f = (x & 9 == 0) <= ((x & 19 != 0) <= (x & A != 0))
        if not f:
            return False
    return True

for A in range(1,10_000):
    if f(A):
        print(A)
        break