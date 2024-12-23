from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[:25]:
    num1 = int('11353'+ x + '12', 25)
    num2 = int('135' + x + '21', 25)
    num = num1 + num2
    if num % 24 == 0:
        print(num//24)