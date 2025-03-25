from itertools import product
count = 0

for i in product('0123456789ABCDEF', repeat = 5):
    i = ''.join(i)
    if i.count('6') == 2 and i.count('06') == 0 and i.count('60') == 0 and i.count('26') == 0 \
            and i.count('62') == 0 and i.count('46') == 0 and i.count('64') == 0 \
            and i.count('86') == 0 and i.count('68') == 0 :
        count += 1
print(count)

