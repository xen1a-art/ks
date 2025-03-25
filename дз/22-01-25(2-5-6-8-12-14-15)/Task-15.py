def plosh(a,b,c):
    return a * b > c

def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (not plosh(x, y, A + 13)) <= (plosh(28, y, 520) or plosh(x, 25, 800))
            if not f:
                return False
    return True

for A in range(-10_000,1000)[::-1]:
    if f(A):
        print(A)
        break

