with open('17_17636.txt') as file:
    data = [int(i) for i in file]

ans = []
max_3 = max(i for i in data if 100 <= abs(i) <= 999 and str(i)[-1] == '3')

for i in range(len(data) - 2):
    a1,a2,a3 = data[i], data[i+1], data[i+2]
    summ = a1+a2+a3

    r1= 100 <= abs(a1) <= 999 and str(a1)[-1] == '3'
    r2= 100 <= abs(a2) <= 999 and str(a2)[-1] == '3'
    r3= 100 <= abs(a3) <= 999 and str(a3)[-1] == '3'
    r = r1 + r2 + r3 >= 1

    t = summ < max_3
    if r and t:
        ans.append(summ)
print(len(ans),max(ans))