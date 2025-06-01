from itertools import product
cnt = 0
for i in product('0123456789', repeat = 5):
    s = ''.join(i)
    if s[0] != '0':
        cnt += 1
        s = s.replace('0', '*')
        s = s.replace('2', '*')
        s = s.replace('4', '*')
        s = s.replace('6', '*')
        s = s.replace('8', '*')
        s = s.replace('1', '-')
        s = s.replace('3', '-')
        s = s.replace('5', '-')
        s = s.replace('7', '-')
        s = s.replace('9', '-')
        if '**' not in s and '--' not in s and cnt % 15 == 0:
            print(cnt,s)









