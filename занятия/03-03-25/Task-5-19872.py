def convert(num,sys):
    res= ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1,10_000):
    r = convert(n,7)
    if n % 2 == 0:
        r = '52' + r + '1'
    else:
        r = r[-1] + r[1:-1] + r[0] + '15'
    r = r.lstrip('0')
    if len(r) == 4 and n <= 1000:
        ans.append(n)
print(max(ans))