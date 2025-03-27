from math import *
ans = []
for i in range(1,10_000):
    izd = ceil((22 * 5 + log2(i))/8)+50
    if izd *i <= 30*1024:
        ans.append(i)
print(max(ans))