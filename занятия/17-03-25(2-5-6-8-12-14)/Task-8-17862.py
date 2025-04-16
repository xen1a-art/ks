from string import digits, ascii_uppercase
from itertools import product

alph = digits + ascii_uppercase
alph = alph[:12]

cnt = 0
for val in product(alph,repeat = 5):
    val = ''.join(val)
    if val.count('7') == 1 and val[0] != '0':
        if val.count('9') + val.count('A') + val.count('B') <= 3:
            cnt += 1
print(cnt)
