def dell(m,n):
    return m & n

def f(a):
    for x in range(1,10_000):
        f = ((x&52!=0)and(x&36==0)) <= (not(x&a==0))
        if not f:
            return False
    return True

for a in range(1,10_000):
    if f(a):
        print(a)
        break
