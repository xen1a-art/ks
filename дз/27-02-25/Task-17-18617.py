with open('17_18617.txt') as file:
    data = [int(i) for i in file]

maxx = max([i for i in data]) % 3
minn = min([i for i in data]) % 7

ans = []
for i in range(len(data) - 1):
    num1,num2 = data[i], data[i+1]
    summ = num1 + num2

    f = num1 % 3 == maxx or  num2 % 3 == maxx

    d= num1 % 7 == minn or num2 % 7 == minn
    if f and d:
        ans.append(summ)
print(len(ans),max(ans))
