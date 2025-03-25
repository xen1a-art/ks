def dell(n,m):
    return n%m == 0

def f(A):
    for x in range(1,100):
        for y in range(1, 100):
            for z in range(1, 100):
                f =(dell(z,115) or dell(y,78) or dell(x,51))<= dell(x,A)
                if not f:
                    return False
    return True

for A in range(1,100)[::-1]:
    if f(A):
        print(A)
        break