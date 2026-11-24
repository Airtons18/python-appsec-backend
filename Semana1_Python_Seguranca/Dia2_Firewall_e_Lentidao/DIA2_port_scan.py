logs_firewall = [
    "192.168.1.50:22:BLOCK",
    "10.0.0.1:80:ALLOW",
    "192.168.1.50:8080:BLOCK",
    "192.168.1.50:3306:BLOCK",
    "172.16.0.5:443:ALLOW",
    "10.0.0.99:21:BLOCK",
    "10.0.0.99:22:BLOCK",
    "10.0.0.99:23:BLOCK",
]

def detectar_port_scan(logs):
    logs_tratado = []
    for ip in logs:
        a = ip.split(':')
        logs_tratado.append(a)
    bloqueios = {}
    for ip in logs_tratado:
        if 'BLOCK' in ip:
            end_ip = ip[0]
            if end_ip not in bloqueios:
                bloqueios[end_ip] = 1
            else:
                bloqueios[end_ip] += 1
    for ip in bloqueios:
        if (bloqueios[ip] >= 3):
            print(ip, bloqueios[ip])
    
detectar_port_scan(logs_firewall)