def divs(num):
    div = set()
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            div |= {i,num//i}
    return sorted(div)

def is_prime(num):
    return num > 1 and not divs(num)

cnt = 0
for num in range(1_273_548,10**10):
    div = divs(num)
    M = sum(div) if div else 0
    if is_prime(M%100_000) and cnt <5:
        print(num,M)
        cnt+=1
        if cnt == 5:
            break
