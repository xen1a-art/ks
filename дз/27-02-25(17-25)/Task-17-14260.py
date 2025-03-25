with open ('17_14260.txt') as file:
    data = ([int(i) for i in file])

minn = min([i for i in data if i > 0 and 1000<= i <= 9999 and str(i)[-1] == str(i)[-2]])

ans = []
for i in range(len(data) - 2):
    a1,a2,a3 = data[i], data[i+1],data[i+2]
    summ = a1+a2+a3

    u1 = 100 <= abs(a1) <= 999
    u2 = 100 <= abs(a2) <= 999
    u3 = 100 <= abs(a3) <= 999

    f2 = u1 + u2 + u3 == 3
    f1 = summ > minn
    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))

