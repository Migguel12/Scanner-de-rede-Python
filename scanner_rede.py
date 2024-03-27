import nmap
import pandas as pd

destino = '10.27.81.0/23'
port = '5985'

nm = nmap.PortScanner()
nm.scan(hosts = destino, ports = port)
if nm.all_hosts():
    print('Host encontrado')
    for host in nm.all_hosts():
        host_ip = host  
        host_state = nm[host_ip].state()
        port_state = nm[host_ip]['tcp'][int(port)]['state']
        print(f'{host_ip} - {host_state} - {port_state}')
        info = {'IP': host_ip, 'Ligado': host_state, 'Status da porta': port_state}
        df = pd.DataFrame(info)
        df.to_csv('lista de máquinas.csv')
else:
    print('Host não encontrado')
