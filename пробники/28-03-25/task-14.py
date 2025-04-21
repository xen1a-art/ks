def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1,2031):
    num = convert(2**2025 + 2**2024 - 2**2021 - x,4)
    ans.append([num.count('0'),x])
print(max(ans))

