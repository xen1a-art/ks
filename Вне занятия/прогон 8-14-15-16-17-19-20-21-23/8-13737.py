from itertools import product

alph = sorted('ДЕКОР')
ans = []
for pos, val in enumerate(product(alph,repeat = 4), start = 1):
    val = ''.join(val)
    if val[0] == 'К':
        ans.append(pos)
print(ans[0])