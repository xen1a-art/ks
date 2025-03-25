from itertools import product

alph = sorted('0123456789')
cnt = 0
for i in product(alph, repeat = 6):
    i = ''.join(i)
    if int(i) % 4 == 0 and len(i) == len(set(i)) and i[0] != '0' :
        for t in range(len(i)- 1):
            if i[t] in alph[::2] and i[t +1] in alph[::2]:
                break
        else:
            cnt += 1
print(cnt)


