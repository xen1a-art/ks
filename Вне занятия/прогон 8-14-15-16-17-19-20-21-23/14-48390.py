ans = []
for x in '01234567':
    for y in '01234567':
        num1 = int(x + '01' + y + '4',9)
        num2 = int(x + y + '544',8)
        num  = num1 + num2
        if num % 89 == 0:
            ans.append(num//89)
if ans:
    print(min(ans))

