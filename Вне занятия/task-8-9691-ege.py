from itertools import product

alph = sorted('ВЛТУ')
cnt = 0
for i in product(alph,repeat = 4):
    i = ''.join(i)
    cnt +=1
    if cnt == 75:
        print(i)