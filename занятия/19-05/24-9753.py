with open('24_9753.txt') as file:
    data = file.readline()

data = data.split('Y')

ans = []
for i in range(len(data) - 150):
    st = 'Y'.join(data[i:i + 151])
    ans.append(len(st))
print(max(ans))