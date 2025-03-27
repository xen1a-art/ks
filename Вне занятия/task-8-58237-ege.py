from itertools import product

alph = '0123456'
cnt = 0
for i in set(product(alph,repeat = 4)):
    i = ''.join(i)
    if i[0] < i[1] < i[2] < i[3]:
        cnt += 1

print(cnt)