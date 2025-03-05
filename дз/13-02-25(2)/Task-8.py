from itertools import product

alph = sorted('ПОКСОДЙЕЛАК')
ans = []

for pos,val in enumerate(product(alph, repeat =6 ), start = 1):
    val = ''.join(val)
    if val[0] == 'К' and val.count('Й') >= 2 and val.count('С') == 0 and val.count('Е') == 0:
        ans.append(pos//2)
print(ans[0])