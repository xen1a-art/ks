with open('24_19254.txt') as file:
    data = file.readline()

data = data.split('FSRQ')
ans = 0
for i in range(len(data) - 80):
    st = 'FSRQ'.join(data[i:i+81])
    ans = max(ans,len(st) + 6)
print(ans)
