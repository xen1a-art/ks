with open('17_20963.txt') as file:
    data = [int(i) for i in file]

min_27 = min([i for i in data if 1000<= abs(i) <= 9999 and abs(i) % 17 == 0])** 2
ans = []

for i in range(len(data) - 2):
    a1,a2,a3 = [data[i],data[i+1],data[i+2]]
    summ1 = abs(a1) + abs(a2) + abs(a3)
    summ = a1**2 + a2**2 + a3 ** 2

    u1 = 1000<= abs(a1) <= 9999 and str(a1)[-2:] == '27'
    u2 = 1000 <= abs(a2) <= 9999 and str(a2)[-2:] == '27'
    u3 = 1000 <= abs(a3) <= 9999 and str(a3)[-2:] == '27'

    u = u1 + u2 + u3 >= 1
    r = summ <= min_27
    if u and r:
        ans.append(summ1)
print(len(ans),min(ans))