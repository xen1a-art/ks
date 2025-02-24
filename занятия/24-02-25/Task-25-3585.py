from itertools import product

ans  = []

for v in '012345678':
    for t in '012345678':
        num = int('1234'+ v + '57'+ t + '8')
        if num % 17 == 0 and num <= 10**9:
            ans.append([num, num//17])

ans = sorted(ans)
for i in ans:
    print(*i)