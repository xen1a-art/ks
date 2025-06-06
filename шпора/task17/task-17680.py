with open('17_17680 (1).txt') as file:
    data = [int(i) for i in file]

min_41 = min(i for i in data if i >0 and i % 41 == 0)
ans = []
for i in range(len(data) - 1):
    a1,a2 = data[i],data[i+1]
    raz = abs(a1-a2)

    r1 = a1 != a2
    r2 = raz % min_41 == 0
    if r1 and r2:
        ans.append(a1+a2)
print(len(ans),max(ans))