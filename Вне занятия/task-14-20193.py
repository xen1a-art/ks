from string import digits, ascii_uppercase

alph = digits + ascii_uppercase
ans = []
for x in alph[:18]:
    num1 = int('11H' +  x + '05',18)
    num2 = int('3F' +  x + '54' + x + '8',18)
    num3 = int('G' +  x + x + x + '9',18)
    num = num1 + num2 + num3
    if num % 14 == 0:
        ans.append(num//14)
print(min(ans))
