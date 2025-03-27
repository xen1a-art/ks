from string import digits, ascii_uppercase

alph = digits + ascii_uppercase
ans = []
for x in alph[:13]:
    num1 = int('4C' + x + '4',15)
    num2 = int( x + '62A',13)
    num = num1 + num2
    if num % 121 == 0:
        ans.append(num//121)
print(ans)

