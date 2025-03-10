def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(1,10_000):
    r = convert(n,4)
    if len(r) % 2 == 0:
        r = r[:len(r)//2] + '0' + r[len(r)//2:]
    r = int(r)
    if r <= 180:
        ans.append(n)
print(max(ans))