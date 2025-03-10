from itertools import *

ans = []
for r in range(5):
    for i in product('0123456',repeat = r):
        i = ''.join(i)
        for t in '123456':
            num_7 = t+'213'+i+'5664'
            num = int(num_7,7)
            if num <= 10**9 and num % 333 == 0:
                ans.append((num,num//333))

ans = sorted(ans)
for i in ans:
    print(*i)