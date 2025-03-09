from itertools import product

ans = []
for r in range(3):
    for i in product('0123456789',repeat = r):
        i=''.join(i)
        for r1 in range(3-r):
            for t in product('0123456789', repeat=r1):
                t = ''.join(t)
                num = int(i+'15'+t+'7424')
                if num <= 10**8 and num % 111 == 0 and num % 113 != 0 and num % 127 != 0:
                    ans.append([num,num//111])
                if num <= 10**8 and num % 113 == 0 and num % 111 != 0 and num % 127 != 0:
                    ans.append([num,num//113])
                if num <= 10**8 and num % 127 == 0 and num % 113 != 0 and num % 111 != 0:
                    ans.append([num,num//127])

ans = sorted(ans)
for i in ans:
    print(*i)