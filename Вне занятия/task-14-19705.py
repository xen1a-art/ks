def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num//=sys
    return res[::-1]

ans = []
for x in range(0,2006):
    num = convert((43**56 + 113**841-x),4)
    if num.count('0') % 2 == 0 and num.count('1') % 2 == 0 and num.count('2') % 2 == 0 and num.count('2') <= 712:
        ans.append(x)
print(max(ans))