def f(x, y, s):
    if x + y >= 81: return s % 2 == 0
    if s == 0: return False
    h = [f(x + 1, y, s - 1),
         f(x * 2, y, s - 1),
         f(x, y + 1, s - 1),
         f(x, y * 2, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)
print('19)', [s for s in range(1,74) if f(7,s,2)])#19
print('20)', [s for s in range(1,74) if f(7,s,3) and not f(7,s,1)])#33,36
print('21)', [s for s in range(1,74) if f(7,s,4) and not f(7,s,2)])#32


