from itertools import product

alph = sorted('ПОБЕДА')

ans = []
for pos,val in enumerate(product(alph,repeat = 6),start= 1):
    val = ''.join(val)
    if val[0] == 'О' and len(set(val)) == 6 and pos %2 == 0:
        ans.append(pos)
print(ans[-1])