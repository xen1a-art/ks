with open('17_21416.txt') as file:
    data = [int(i) for i in file]

summ = sum([i for i in data if i < 0])
ans = []

for i in range(len(data) - 2):
    table = [data[i],data[i+1],data[i+2]]

    r = max(table) * min(table)
    t = r > summ
    if t:
        ans.append(sum(table))
print(len(ans),max(ans))
