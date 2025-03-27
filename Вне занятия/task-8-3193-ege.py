from itertools import product

alph = sorted('АОУ')

cnt = 0
for i in product(alph,repeat = 5):
    i = ''.join(i)
    cnt += 1
    if cnt == 210:
        print(i)