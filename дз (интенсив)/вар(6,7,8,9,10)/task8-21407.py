from itertools import product

alph = 'ДГИАШЭ'
cnt = 0
for i in product(alph, repeat= 5):
    i = ''.join(i)
    if i[0] != 'И' and i[0] != 'Э' and i[0] != 'А' and i[-1] != 'Д' and i[-1] != 'Г' and i[-1] != 'Ш':
        cnt +=1
print(cnt)