from itertools import product

alph = '0123456789ABCDE'
ans = []
for val in product(alph,repeat =7):
    val = ''.join(val)
    if val.count('0')== 2 and val.count('A') + val.count('B') +val.count('C') + val.count('D') + \
            val.count('E') <= 3 and val[0] != '0' :
        ans.append(val)
print(len(ans))