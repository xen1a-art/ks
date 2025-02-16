with open ('17_17873.txt') as file:
    data = [int(i) for i in file]

minn = min(data)
ans = []

for i in range(len(data) - 1 ):
    a1,a2 = data[i], data[i + 1]

    osta1 = a1 % 16 == minn
    osta2 = a2 % 16 == minn

    if osta1 + osta2 >= 1:
        ans.append(a1 + a2)
print(len(ans), max(ans))

