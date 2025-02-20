from itertools import product

ans = []

for v in '0123456789':
    for t in '0123456789':
        for N in '13579':
            for C in '02468':
                for F in '02468':
                    num = int(C + '9'+ v + '23'+ t + '23' + N + F)
                    if num % 1984 == 0 and num <= 10**10:
                        ans.append([num,num//1984])

ans = sorted(ans)
for i in ans:
    print(*i)