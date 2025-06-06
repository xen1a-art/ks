from itertools import product
cnt =0
alph = '012345678'

for i in product(alph, repeat = 5):
    i = ''.join(i)
    if i[0] != '0' and i.count('0') == 1:
        i = i.replace('1', '*')
        i = i.replace('3', '*')
        i = i.replace('5', '*')
        i = i.replace('7', '*')
        if '*0*' not in i and '*0' not in i and '0*' not in i:
            cnt += 1
print(cnt)


