def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num//=sys
    return res[::-1]

ans = []
for n in range(1,10_000):
    r = convert(n,3)
    sm = sum(map(int,r))
    if sm % 2== 0:
        r = '1' + r + '2'
    else:
        r = '2'+ r + '0'
    r = int(r,3)
    if r > 100:
        ans.append(r)
print(min(ans))
