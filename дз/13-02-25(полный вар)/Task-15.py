def dell(m,n):
    return m & n

def f(a):
    for x in range(90,100):
        f = (not(x&79 == 0)) and ((x&31== 0) <= (not(x&a == 0)))
        if not f:
            return False
    return True

for a in range(0,10_000):
    if f(a):
        print(a)
        break

