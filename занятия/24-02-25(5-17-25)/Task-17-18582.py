with open('17_18582.txt') as file:
    data = [int(i) for i in file]

minn = min(data)

ans =[]
for i in range(len(data) -2):
    num1,num2, num3 = data[i], data[i + 1], data[i + 2]

    u1 = num1 < 0
    u2 = num2 < 0
    u3 = num3 < 0

    if u1 + u2 + u3 >= 2:
        if str(u1 + u2 +u3)[-1] == minn:
            ans.append(abs(num1 + num2+ num3))
print(len(ans), max(ans))