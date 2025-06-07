from doctest import master

with open('17 (1).txt') as file:
    data = [int(i) for i in file]

ans = []

for i in range(len(data) - 1):
    a1,a2 = [data[i],data[i+1]]
    sum1 = a1 + a2
    proz = a1 * a2

    u1 = proz % 34 != 0

    if u1 :
        ans.append(sum1)
print(len(ans),max(ans))


