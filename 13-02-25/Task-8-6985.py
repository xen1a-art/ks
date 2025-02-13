from itertools import product

alph = sorted('МАРКСЛ')
ans = []
for pos,val in enumerate(product(alph, repeat = 6), start = 1):
    val = ''.join(val)
    if val.count('СК') == 0 and val.count('КС') == 0 and val.count('К') or val.count('С') \
            or val.count('М') or val.count('А') or val.count('Р') or val.count('Л') == 3:
        ans.append(pos)
print(ans[-1])