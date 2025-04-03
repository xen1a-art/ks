def f(x,y,s):
    if x + y >= 44: return s%2 ==  0
    if s == 0: return 0
    hod = [f(x+y,y,s-1),
           f(x,x+y,s-1)]
    return any(hod) if (s-1) % 2 == 0 else all(hod)

print('19)',[i for i  in range(45) if f(11,i,1)])
print('20)',[i for i  in range(45) if f(11,i,2)])

ans = []
for s1 in range(1,44):
    for s2 in range(1, 44):
        if f(s1,s2,3):
            ans.append([abs(s1-s2),s1,s2])
print('21)',min(ans))

