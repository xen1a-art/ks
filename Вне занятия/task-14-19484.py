num = 5*729**2024+3*243**1413-7*81**169-2*9**107+3017
cnt = 0
while num:
    if num % 27 <= 25 and (num % 27 )% 2 ==0:
        cnt += num % 27
    num //= 27
print(cnt)
