def is_prime(num):
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def f(num):
    divs = set()
    for i in range(2,int(num**0.5) + 1):
        if num %  i == 0:
            if is_prime(i) : divs.add(i)
            if is_prime(num//i): divs.add(num//i)
    divs = sorted(divs)

    if len(divs) < 2:
        return 0
    return sum(divs)

cnt = 0
for i in range(32_500_000,10**20):
    m = f(i)
    if m != 0 and m % 145 == 0:
        print(i,m)
        cnt += 1
        if cnt == 7:
            break
