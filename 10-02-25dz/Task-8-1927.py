from itertools import product

alph = sorted('ЯСНОВИДЕЦ')
ans = []
for pos,val in enumerate(product(alph, repeat = 5), start = 1):
    val = ''.join(val)
    if val[0] in 'СНВДЦ' and val[-1] in 'ЯОИЕ' and val[0] not in val[1:] and val[-1] not in val[:-1]:
        ans.append(pos)
print(len(ans))