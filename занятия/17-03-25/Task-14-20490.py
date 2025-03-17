for x in range(0,2006):
    num = 4**163 * 5 + 12**62 - x
    cnt1,cnt4 = 0,0
    while num:
        if num > 0:
            if num % 5 == 1:
                cnt1 += 1
            if num % 5 == 4:
                cnt4 += 1
        num //= 5
    if cnt1 < cnt4:
        print(x)