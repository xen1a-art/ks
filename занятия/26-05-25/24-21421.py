# 21421 реплейс
from string import ascii_uppercase

with open('24_21421.txt') as file:
    data = file.readline()

for i in ascii_uppercase[2:]:
    data = data.replace(i, ' ')

data = data.split()

ans = 0
for i in data:
    i = i.strip('0')
    if i and int(i, 12) % 2 == 0:
        ans = max(ans, len(i))
    else:
        for l in range(len(i)):
            for r in range(len(i), l, -1):
                sub_str = i[l:r].strip('0')
                if sub_str and int(sub_str, 12) % 2 == 0:
                    ans = max(ans, len(sub_str))
                    break
print(ans)