from itertools import product

alph = sorted('ДГИАШЭ')

ans = []
for pos,val in enumerate(product(alph,repeat = 5), start = 1):
    val = ''.join(val)
    if val[0] not in 'ИАЭ' and val[-1] not in 'ДГШ':
        ans.append(pos)
print(len(ans))