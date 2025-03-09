from itertools import product

ans = []
for r in range(6):
    for i in product('02468', repeat = r):
        i=''.join(i)
        for t in '13579':
            for t1 in '13579':
                num = int(i+'12'+t+'4'+t1)
                if num <= 10**10 and num % 9231 == 0:
                    ans.append([num,num//9231])

ans = sorted(ans)
for i in ans:
    print(*i)
