def f(num):
    div = set()
    for i in range(2,int(num**0.5)+ 1):
        if num % i == 0:
            div.add(i)
            div.add(num//i)
    div = sorted(div)

    for i in div:
        if str(i)[-1] == '7' and i != num and i != 7:
            return i
    return 0

cnt =0
for i in range(700_001, 10 ** 15):
    r = f(i)
    if r:
        print(i,r)
        cnt += 1
        if cnt == 5:
            break