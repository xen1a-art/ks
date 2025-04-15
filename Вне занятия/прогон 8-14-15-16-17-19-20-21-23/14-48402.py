ans = []

for x in '0123456789':
    num1 = int('3' + x + 'DA',14 )
    num2 = int('5' + x + 'A6',12 )
    num = num1 + num2
    if num % 81 == 0:
        ans.append(num//81)
print(ans)