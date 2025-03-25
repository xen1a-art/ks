def dell(x,y):
    return x % y == 0

def f(A):
    for x in range(1,10_000):
        f = ((not dell(x,7)) and dell(x,13)) <= (x > A - 40)
        if not f:
            return False
    return True

for A in range(1,10_000)[::-1]:
    if f(A):
        print(A)
        break