with open('1706.txt') as file:
    data = [int(i) for i in file]

min_19 = min([i for i in data if str(i)[-2:] == '19' and 100<=i<=999 ])
ans = []

for i in range(len(data) - 2 ):
    a1,a2,a3 = data[i], data[i + 1], data[i + 2]
    summ = a1 + a2 + a3

    u1 = 10000<=a1<=99999 and str(a1)[-2:] == '19'
    u2 = 10000<=a2<=99999 and str(a2)[-2:] == '19'
    u3 = 10000<=a3<=99999 and str(a3)[-2:] == '19'

    f1= u1 + u2 + u3 >= 1
    f2 = summ > min_19 ** 2
    if f1 + f2:
        ans.append(summ)
print(len(ans),min(ans))