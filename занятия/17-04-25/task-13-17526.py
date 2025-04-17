from ipaddress import ip_network
net = ip_network('172.16.128.0/255.255.192.0')

cnt = 0
for i in net:
    i = f'{int(i):032b}'
    if i.count('1') % 2 != 0:
        cnt += 1
print(cnt)

#print(net.hosts())# узлы текущей сети
#print(net.network_address)#адрес сети
#print(net.netmask)#маска сети
#print(net.broadcast_address)# широковещательный адрес
#print(net.num_addresses)# кол-во адресов (адрес сети+ широковещательный+ узлы)