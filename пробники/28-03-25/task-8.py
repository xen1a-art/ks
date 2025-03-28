from itertools import product

alph = sorted('ЛУНАТИК')
ans = []
for pos,val in enumerate(product(alph,repeat = 6)):
    val = ''.join(val)
    if val[0] == 'Н' and (val.count('У') == 1 or val.count('А') == 1 or val.count('И') == 1):
        ans.append(pos)
print(ans[-1])