def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res [::-1]

num = 3* 3125**9 + 2*625**8 - 4*625**7 + 3*125**6 - 2 * 25**5 - 2024
print(convert(num,25).count('0'))