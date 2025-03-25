ans = []
for n in range(123_456_789,456_789_013):
    r= bin(n)[2:]
    if n % 2 == 0:
        r = '11' + r
    else:
        r = '1' + r + '10'
    r = int(r,2)
    ans.append(r)
print(max(ans))