from ipaddress import ip_network

net = ip_network('112.160.0.0/255.240.0.0')
cnt = 0
for i in net:
    i = f'{int(i):032b}'
    if i.count('1') % 3 != 0:
        cnt+=1
print(cnt)