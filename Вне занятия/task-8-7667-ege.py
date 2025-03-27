from itertools import product

alph = 'ЕГЭ'
cnt = 0
for i in set(product(alph,repeat = 5)):
    i = ''.join(i)
    if i[0] == 'Е' or i[0] == 'Э':
        cnt += 1
print(cnt)