with open('17_17680.txt') as file:
    data = [int(i) for i in file]
ans = []
min_41= min([i for i in data if i > 0 and i % 41 == 0])

for i in range(len(data) - 1):
    a1,a2 = data[i], data[i+1]
    p = abs(a1- a2)

    f1 = a1 != a2
    f2 = p % min_41 == 0
    if f1 and f2:
        ans.append(a1+a2)
print(len(ans),max(ans))

