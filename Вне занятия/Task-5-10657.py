def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(0,1000):
    u = convert(n,3)
    r = sum(int(i) for i in u)
    if r % 3 ==0:
        r = '20' + str(u)
    else:
        r = '10'+ str(u)
    r = int(r,3)
    if r < 100:
        ans.append(n)
print(max(ans))