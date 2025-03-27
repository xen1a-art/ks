from itertools import product

alph = 'слон'
cnt = 0
for i in set(product(alph,repeat = 5)):
    i = ''.join(i)
    if i.count('с') == 1:
        cnt += 1
print(cnt)