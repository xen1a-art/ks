def mod(m, n):
    return m % n


def f(A):
    for x in range(1, 10_000):
        f = (A + x > 700 - A) and (mod(A, 100) + mod(100, x) > 50)
        if not f:
            return False
    return True


for A in range(1, 10_000):
    if f(A):
        print(A)
        break
