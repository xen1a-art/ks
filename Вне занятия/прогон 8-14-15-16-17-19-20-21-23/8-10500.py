from itertools import product

alph = '12345'
ans = []
for pos,val in enumerate(product(alph, repeat = 5), start = 1):
    val = ''.join(val)
    if val.count('1') == 3:
        ans.append(pos)
print(len(ans))
