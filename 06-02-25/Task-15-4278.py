def dell(n,m):
    return n % m == 0

def f(A):
    for x in range(1,10_000):
        f = dell(A,12) and (dell(530, x) <= ((not(dell(A,x))) <= (not(dell(170,x)))))
        if not f:
            return False
    return True

for A in range(1,1000):
    if f(A):
        count = sum(f(A) for A in range(1,1000))
        print(count)
        break