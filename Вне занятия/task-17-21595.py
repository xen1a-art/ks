with open('17_21595.txt') as file:
    data = [int(i) for i in file]

kolich = len([i for i in data if str(i)[-1] == '3' and 1000 <= abs(i) <= 9999])
ans = []

for i in range(len(data) - 2):
    table = [data[i], data[i+1],data[i+2]]


    t = sum(table) - min(table)
    r = kolich ** 2
    u = t > r
    if u:
        ans.append(sum(table))
print(len(ans),max(ans))