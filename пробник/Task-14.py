from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
alph = alph[:26]

for x in alph:
    num_1 = int('27'+ x + '98876', 26)
    num_2 = int('26' + x + '51', 26)
    num_3 = int('15'+ x + '47', 26)
    num_4 = int('62' + x + '5', 26)
    num = num_1 + num_2 + num_3 + num_4
    if num % 25 == 0:
        print(num//25)