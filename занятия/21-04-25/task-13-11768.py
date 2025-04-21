from ipaddress import ip_network, ip_address

for mask in range(16,25):
    ip = ip_address(f'143.172.12.114')
    net = ip_network(f'143.172.8.0/{mask}',False)
    if ip in net.hosts() and net.network_address == ip_address("143.172.8.0"):
        print(net.netmask)