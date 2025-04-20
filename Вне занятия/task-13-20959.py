from ipaddress import ip_network
net = ip_network('203.68.128.0/255.255.192.0')

cnt = 0
for i in net:
    i = f'{int(i):032b}'
    if i.count('1')% 7 != 0:
        cnt += 1
print(cnt)