from itertools import product

alph = sorted('ABCDEF')
ans = []

for pos,val in enumerate(product(alph, repeat = 6),start = 1):
    val = ''.join(val)
    if val[0] != 'A' and val[5] != 'A' and val[0] != 'E' and val[5] != 'E':
        ans.append(pos)

print(ans[-1])