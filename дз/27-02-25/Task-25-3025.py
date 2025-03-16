def divs(num):
    div = set()
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            div |= {i,num//i}
    return sorted(div)

cnt = 0
for num in range(200_000_001,10**11):
    div = [i for i in divs(num) if i % 2 == 1 ]
    D = div[-6] if len(div) >= 6 else 0
    if D > 0 and cnt < 5:
        print(num,D)
        cnt += 1
        if cnt == 5:
            break