from itertools import product
count = 0

for i in product('0123456789AB', repeat = 7):
    i = ''.join(i)
    if i.count('B') == 2 and i[0] in '02468A' and i[1] in '13579B' and i[2] in '02468A' \
            and i[3] in '13579B' and i[4] in '02468A' and i[5] in '13579B' and i[6] in '02468A':
        count += 1
print(count)
