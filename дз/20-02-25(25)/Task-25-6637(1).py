from itertools import product

ans = []
for r in range(0,4):
    for i in product('0123456789', repeat = r):
        i = ''.join(i)
        for t in '0123456789':
            num = int('1'+t+'2139'+i+'4')
            if num % 3052 == 0 and num <= 10**10:
                ans.append([num,num//3052])
ans = sorted(ans)
for i in ans:
    print(*i)