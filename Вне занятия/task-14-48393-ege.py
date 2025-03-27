ans = []
for x in '01234567':
    for y in '01234567':
        num1 = int(y + '04' + x + '5',11)
        num2 = int('253' + x + y,8)
        num = num1 + num2
        if num % 117 == 0:
            ans.append(num//117)
print(ans)
