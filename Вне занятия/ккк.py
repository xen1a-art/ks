def f(x,s):
    if x >= 40:
        return s % 2 == 0
    if s == 0:
        return False
    hod = [f(x + 1,s-1),f(x+4,s-1),f(x*2,s-1)]
    return any(hod) if (s-1) %2 == 0 else all(hod)
print([s for s in range(1,40),])
