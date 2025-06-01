def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1,10_001):
    num1 = convert(6**900 + 6**10 - x,6)
    if num1.count('3') == num1.count('5'):
        ans.append(x)
print(max(ans))