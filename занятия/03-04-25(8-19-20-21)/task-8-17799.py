from itertools import product

alph = sorted('АРГУМЕНТ')
ans = []
for pos,val in enumerate(product(alph,repeat = 4),start = 1):
    val = ''.join(val)
    if len(val) == len(set(val)):
        if val ==''.join(sorted(val)):
            ans.append(pos)
print(ans[-1])