from itertools import product

alph = sorted('БЕЛКА')
ans = []
for pos,val in enumerate(product(alph,repeat = 4),start = 1):
    val = ''.join(val)
    if val.count('Б') == 1:
        ans.append(pos)
print(len(ans))