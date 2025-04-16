def f(A):
    for x in range(1,10_000):
        for y in range(1, 10_000):
            f = (x * y < A) or (y > x) or (x >= 8)
            if not f:
                return False
    return True
for A in range(1,10_000):
    if f(A):
        print(A)
        break