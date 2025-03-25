from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
alph = alph[:35]

for x in alph:
    num_1 = int('6'+ x + 'QR' + x, 35)
    num_2 = int(x + '59' + 'SH', 35)
    num_3 = int('PH'+ x + '69' + 'YW', 35)
    num = num_1 + num_2 + num_3
    res = []
    for i in '0123456789':
        res.append([str(num).count(i),i])
    ans = (9- res[::-1].index(max(res)))** 2
    if num % ans == 0:
        print(num//ans)