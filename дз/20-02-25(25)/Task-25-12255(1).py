from itertools import product

ans = []
for r in range(3):
    for i in product('0123456789',repeat = r):
        i = ''.join(i)
        for t in '0123456789':
            for t1 in '0123456789':
                for t2 in '0123456789':
                    num = int('12'+t+'3'+i+'456'+t1+t2+'9')
                    if num <= 10**12 and num % 98591== 0:
                        ans.append([num,num//98591])
ans = sorted(ans)
for i in ans:
    print(*i)