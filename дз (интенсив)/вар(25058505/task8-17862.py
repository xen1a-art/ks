from itertools import product

alph = '0123456789AB'
cnt  =0

for i in product(alph,repeat = 5):
    i = ''.join(i)
    u = len([j for  j in i if j not in '012345678'])
    if i[0] != '0' and i.count('7') == 1 and u <= 3:
        cnt += 1
print(cnt)