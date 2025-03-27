ans = []
for x in '012345678':
    for y in '012345678':
        num1 = int('2' + y + '66' + x,9)
        num2 = int( x + '0' +y + '1',12)
        num = num1 + num2
        if num % 170 == 0:
            ans.append(num//170)
print(ans)