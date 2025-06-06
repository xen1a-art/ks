with open('17_17873.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data)
ans = []
for i in range(len(data) - 1):
    a1,a2 = data[i],data[i+1]

    r1 = a1 % 16
    r2 = a2 % 16
    r = r1 + r2 >= 1
    t = r == minn
    if t:
        ans.append(a1+a2)
print(len(ans),max(ans))
