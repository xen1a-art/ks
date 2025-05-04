from itertools import product

cnt = 0
alph = '01234567'

for pos in set(product(alph, repeat = 6)):
    pos = ''.join(pos)
    if pos[0] != '0' and int(pos,8)%5 == 0 and len(pos) == len(set(pos)):
        pos = pos.replace('0','!')
        pos = pos.replace('2','!')
        pos = pos.replace('4', '!')
        pos = pos.replace('6', '!')
        pos = pos.replace('1','*')
        pos = pos.replace('3','*')
        pos = pos.replace('5','*')
        pos = pos.replace('7','*')
        if '!!' not in pos:
            if '**' not in pos:
                cnt+=1
print(cnt)





