with open ('17_4705.txt') as file :
    data = [int(i) for i in file ]

max_3 = max([i for i in data if str(i)[-1:] == '3'])
ans = []

for i in range(len(data) - 1):
    a1,a2 = data[i], data[i + 1]
    summ = a1 **2 + a2 **2

    f1 = str(a1)[-1:] == '3'
    f2 = str(a2)[-1:] == '3'

    u1 = f1 + f2 == 1
    u2 = summ >= max_3 **2

    if u1 and u2:
        ans.append(summ)
print(len(ans), max(ans))