def f(A):
    for x in range(0,10_000):
        for y in range(0, 10_000):
            f = (x - 3*y < A) or ( y > 400) or (x > 56)
            if not f:
                return False
    return True

for A in range(0,100):
    if f(A):
        print(A)
        break
