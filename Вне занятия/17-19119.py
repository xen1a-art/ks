with open('17_19119.txt') as file:
    data = [int(i) for i in file]

ans = []
minn = min([i for i in data])

for i in range(len(data) - 1):
    a1,a2 = data[i],data[i+1]
    r= abs(a1-a2)

    t1 = a1 % 43 == minn
    t2 = a2 % 43 == minn
    if t1 and t2:
        ans.append(r)
print(len(ans),max(ans))

