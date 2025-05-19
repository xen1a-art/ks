ans = []
for n in range(2,10_000):
    r = bin(n)[2:]
    cnt = 0
    cnt1 = 0
    for i in range(len(r)):
        if (i+1) % 2 == 0 and r[i] == '1':
            cnt += 1
        if (i+1) % 2 != 0 and r[i] == '0':
            cnt1 += 1
    r = abs(cnt-cnt1)
    if r == 5:
        ans.append(n)
print(min(ans))