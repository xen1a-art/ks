with open('17_18045.txt') as file:
    data = [int(i) for i in file]
ans = []
col = len([i for i in data if 10 <= i <= 99])

for i in range(len(data) - 1):
    a1,a2 = data[i],data[i+1]
    summ = int(str(a1)[-1]) + int(str(a2)[-1])

    f = summ == col
    if f:
        ans.append(a1+a2)
print(len(ans),min(ans))
