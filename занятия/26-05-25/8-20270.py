from itertools import product

alph= '0123456'
cnt = 0
for i in set(product(alph, repeat = 5)):
    i =''.join(i)
    if i[0] != 0:
        i = i.replace('0','*')
        i = i.replace('2','*')
        i = i.replace('4','*')
        i = i.replace('6','*')
        if i.count('**') >= 2 and '***' not in i:
            cnt += 1
print(cnt)
