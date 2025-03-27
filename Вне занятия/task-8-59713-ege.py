from itertools import product

alph = 'ПЯТНИЦА'
cnt = 0
for i in set(product(alph,repeat = 5)):
    i = ''.join(i)
    if i.count('Я') == 1 and i[0] != 'Н' :
        cnt+= 1
print(cnt)