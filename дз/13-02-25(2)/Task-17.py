with open ('17.txt') as file:
    data = [int(i) for i in file]

ans= []
max_50 = max([i for i in data if str(i)[-2:] == '50'])

for i in range(len(data) - 2):
    a1,a2,a3 = data[i], data[i + 1], data[i+2]
    summ = a1+a2+a3

    u1 = 10000 <= abs(a1) <= 99999
    u2 = 10000 <= abs(a2) <= 99999
    u3 = 10000 <= abs(a3) <= 99999

    f1 = summ <= max_50
    f2 = u1 + u2+ u3 == 3
    f3 = a1 != a2 != a3 != a1
    if f1 and f2 and f3:
        ans.append(summ)
print(len(ans),max(ans))

