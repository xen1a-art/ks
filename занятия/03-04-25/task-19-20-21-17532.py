def f(x,y,s):
    if x + y >= 65: return s % 2 == 0
    if s == 0: return False
    hod = [f(x + 1,y,s-1),
           f (x * 3,y,s-1),
           f(x ,y+ 1,s-1),
           f(x,y*3,s-1)]
    return any(hod) if (s-1)% 2 == 0 else any(hod)

print('19)', [i for i in range(1,59) if f(6,i,2)])#7
print('20)', [i for i in range(1,59) if f(6,i,3) and not f(6,i,1)])#12
print('21)', [i for i in range(1,59) if f(6,i,4) and not f(6,i,2)])#1