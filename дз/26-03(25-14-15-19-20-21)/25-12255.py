from itertools import product

ans = []
for r in range(3):
    for f in product('0123456789', repeat = r):
        f = ''.join(f)
        for a in '0123456789':
            num = int('12' + a + '3' + f + '456'+ a+a+'9')
            if num % 98591 == 0 and num <= 10**12:
                ans.append([num,num//98591])
ans = sorted(ans)
for i in ans:
    print(*i)