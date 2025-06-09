def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]

num = 4*625**1920+4*125**1930-4*25**1940-3*5**1950-1960
print(convert(num,5).count('0'))