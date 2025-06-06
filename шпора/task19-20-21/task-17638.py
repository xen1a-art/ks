def f(x,s):
    if x>= 39:
        return s % 2 == 0
    if s == 0:
        return False
    hod = [f(x+1,s-1),
           f(x+3,s-1),
           f(x*2,s-1)]
    return any(hod) if (s-1)%2 == 0 else all(hod)

print('19)', [i for i in range(1,39) if f(i,2)])
print('20)', [i for i in range(1,39) if f(i,3) and not f(i,1)])
print('21)', [i for i in range(1,39) if f(i,4) and not f(i,2)])