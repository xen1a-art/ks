def f(x,s):
    if x >= 67: return s % 2 == 0
    if s == 0: return False
    hod = [f(x+1,s-1),
           f(x+3,s-1),
           f(x*2,s-1)]
    return any(hod) if (s-1)%2 == 0 else all(hod)
print('19)', [s for s in range(1,67) if f(s,2)])
print('20)', [s for s in range(1,67) if f(s,3) and not f(s,1)])
print('21)', [s for s in range(1,67) if f(s,4) and not f(s,2)])