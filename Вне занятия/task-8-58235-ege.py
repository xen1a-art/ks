from itertools import product

alph = '0123'
cnt = 0

for i in set(product(alph,repeat = 3)):
    i = ''.join(i)
    if (int(i[0]) + int(i[2]) > int(i[1])) and i[0] != '0':
        cnt += 1
print(cnt)