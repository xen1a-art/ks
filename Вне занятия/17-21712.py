with open('17_21712.txt') as file:
    data = [int(i) for i in file]

ans = []
min_6 = min([i for i in data if 1000 <= i <= 9999 and str(i)[-1] == '6' and i> 0])

for i in range(len(data)- 2):
    a1,a2,a3 = data[i], data[i+1],data[i+2]
    summ = a1 + a2+ a3

    t1 = 1000 <= abs(a1) <= 9999 and str(a1)[-1] == '6'
    t2 = 1000 <= abs(a2) <= 9999 and str(a2)[-1] == '6'
    t3 = 1000 <= abs(a3) <= 9999 and str(a3)[-1] == '6'

    f1 = t1 + t2 + t3 == 1
    f2 = summ <= min_6
    if f1 and f2:
        ans.append(summ)
print(len(ans),max(ans))



