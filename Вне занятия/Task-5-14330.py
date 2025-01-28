ans = []
for n in range(10_000,100_000):
    r = (max(int(i) for i in str(n)) + min(int(i) for i in str(n)))**2
    p = 1
    for i in str(n):
        if int(i)%2 == 0:
            p *= int(i)
    d = str(max(p,r)) + str(min(r,p))
    if d == '121 16':
        ans.append(n)
print(min(ans))




