from itertools import product

alph = '0123456789ABCDE'
ans = []
for val in product(alph, repeat = 5):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1 and len([i for i in val if i not in '0123456789']) >= 2:
        ans.append(val)
print(len(ans))