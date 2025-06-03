def f(x,y,s):
    if x + y <= 72: return s % 2 == 0
    if s == 0: return False
    hod = [f(x-3,y,s-1),
           f(x//2,y,s-1),
           f(x,y-3,s-1),
           f(x,y//2,s-1)]
    return any(hod) if (s-1)%2 == 0 else all(hod)
print('19)', [s for s in range(1,73) if f(50,s,2)])


if num % 2 == 0 else num //2