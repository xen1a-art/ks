def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]
print(convert(125**4+25**8-30, 5).count('4'))