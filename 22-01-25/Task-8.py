from itertools import product
count = 0
t = '02468A'
r = '13579B'
e = '2468A'
for i in product('0123456789AB', repeat = 7):
    i = ''.join(i)
    if i.count('B') == 2 and i[0] in e and i[1] in r and i[2] in t and i[3] in r and i[4] in t and i[5] in r \
            and i[6] in t or i.count('B') == 2 and i[0] in r and i[1] in t and i[2] in r and i[3] in t and i[4] in r and i[5] in t \
            and i[6] in r :
        count += 1
print(count)

