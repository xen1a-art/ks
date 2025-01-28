def dell(n,m):
    return n % m == 0

def f(A):
    for x in range(1, 1000):
        f = (dell(A, x ) <= ((x == A) or (x == 1)))
        if not f:
            return False
    return True

for A in range(1, 11_111):
    if f(A):
        count = sum(f(A) for A in range(1, 11_111))
        print(count)
        break
