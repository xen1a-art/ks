def divs(num):
    div = set()
    for i in range(2,int(num**0.5)+ 1):
        if num % i == 0:
            div |= {i,num//i}
    return sorted(div)



cnt = 0
for num in range(1_200_000,0,-1):
    div = divs(num)
    S = sum(div[-3:]) if len(div) >=3 else 0
    if S != 0 and S % 2022 == 0 and S != num and cnt < 5:
        print(num,S)
        cnt += 1
        if cnt == 5:
            break



