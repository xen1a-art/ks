from itertools import product

alph = sorted('ИНСТАВК')
cnt = 0
for val in product(alph, repeat = 4):
    val = ''.join(val)
    if  val[-1] == 'Н' or val[-1] == 'С' or val[-1] == 'Т' or val[-1] == 'В' or val[-1] == 'К' \
        or val[0] == 'И' or val[0] == 'А' :
        continue
    cnt+= 1
    if val == 'НИКА':
        print(cnt)

