logs_servidor = [
    "192.168.1.10:/login:120",
    "10.0.0.5:/home:45",
    "LINHA_CORROMPIDA_SEM_DOIS_PONTOS",
    "192.168.1.10:/admin:2500",
    "172.16.0.2:/produtos:ERRO",
    "10.0.0.99:/busca:4800",
    "",
    "192.168.1.10:/checkout:3100",
]

def detectar_lentidao(logs):
    logs_limpo = []
    for ip in logs:
        p1 = ip.split(':')
        logs_limpo.append(p1)
    suspeitos_lentidao = []
    linhas_sujas = 0
    for ip in logs_limpo:
        try:
            if (len(ip) == 3):
                if (ip[2].isdigit() == True):
                    p1 = (int(ip[2]))
                    if p1 >= 2000:
                        suspeitos_lentidao.append(ip)
                else:
                    linhas_sujas += 1
            else:
                linhas_sujas += 1
                print('Linhas Sujas: ', linhas_sujas)
        except Exception:
            print(Exception)
    print('Suspeitos de lentidão:', suspeitos_lentidao)
    print('Total de linhas sujas:', linhas_sujas)

detectar_lentidao(logs_servidor)