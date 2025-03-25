def f(A):
    for x in range(0, 1000):
        f = (x & A == 0) or (not(x & 37 == 0)) or (not(x & 12 == 0))
        if not f:
            return False
    return True

for A in range(0, 1000)[::-1]:
    if f(A):
        print(A)
        break