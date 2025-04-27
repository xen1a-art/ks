def f(A):
    for x in range(1,10_000):
        for y in range(1, 10_000):
            f = not ((x<7) or (y >= 3*x + A - 20) or (x >= 34) or (y < 121))
            if f:
                return False
    return True

for A in range(1,10_000)[::-1]:
    if f(A):
        print(A)
        break
