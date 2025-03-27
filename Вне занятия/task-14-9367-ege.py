def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]
print(convert(9**8 + 3**5 - 9,3).count('2'))