cnt = 0
def dell(num):
    dells = set()
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            dells.add(i)
            dells.add(num//i)
    return dells

def prime(num):
    return  num > 1 and not dell(num)

for i in range(1_200_001,10**20):
    if not prime(i):
        dells = [r for r in dell(i) if prime(r)]
        if len(dells) != 0:
            m = max(dells) + min(dells)
        else:
            m = 0
        if m > 2000 and str(m)[-1:] == '8':
            cnt += 1
            print(i,m)
    if cnt == 5:
        break