with open('17_19249.txt') as file:
    data =[int(i) for i in file]

ans = []
max_43 = (max([i for i in data if 10_000 <= abs(i) <= 99_999 and str(i)[-2:] == '43']))**2

for i in range(len(data) - 2):
    a1,a2,a3 = data[i],data[i+1],data[i+2]
    summ = a1 **2 + a2**2 + a3 ** 2

    t1 = 10_000 <= abs(a1) <= 99_999 and str(a1)[-2:] == '43'
    t2 = 10_000 <= abs(a2) <= 99_999 and str(a2)[-2:] == '43'
    t3 = 10_000 <= abs(a3) <= 99_999 and str(a3)[-2:] == '43'

    f1 = t1 + t2 +t3 >= 1
    f2 = summ <= max_43
    if f1 and f2:
        ans.append(summ)
print(len(ans),min(ans))