def divs(num):
    div = set()
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            div |= {i,num//i}
    return sorted(div)


cnt = 0
for num in range(220_001,10**9):
    div = divs(num)
    M = max(div) + min(div) if div else 0
    if M % 10 == 4 and cnt <5:
        print(num,M)
        cnt += 1
        if cnt == 5:
            break