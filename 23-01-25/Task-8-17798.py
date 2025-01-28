from itertools import product

alph = sorted('МИНУС')
ans = []
for pos,val in enumerate(product(alph, repeat = 4), start = 1):
    val = ''.join(val)
    if val.count('М') + val.count('Н') == 2 or val.count('М') + val.count('С') == 2 or val.count('С') + val.count('Н') == 2 and val.count('И') + val.count('У') == 2:
        ans.append(pos)

print(ans[-1])

