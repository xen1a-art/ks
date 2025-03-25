from itertools import product

ans = []
for r in range(0,5):
    for i in product('0123456789', repeat = r):
        i = ''.join(i)
        for v in '0123456789':
            num = int('12' + i + '567' + v)
            if num % 7777 == 0 and sum([num+1])% 2 != 0 and num <= 10**10:
                ans.append([num,num//7777])
ans = sorted(ans)
for i in ans:
    print(*i)
