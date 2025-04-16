def dell(n,m):
    return n % m == 0

def f(A):
    for x in range(1,10_000):
        for y in range(1, 10_000):
            f = (dell(144,x) <= (not(dell(x,y)))) or (x + y > 100)or (A - x > y)
            if not f:
                return False
    return True

for A in range(1,10_000):
    if f(A):
        print(A)
        break