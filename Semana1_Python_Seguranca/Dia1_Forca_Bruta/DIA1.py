'''
Sua Missão (Escrever do zero, na mão):

Crie uma função chamada detectar_forca_bruta(logs) que receba essa lista logs_acesso e faça o seguinte:

Conte quantas vezes cada ip teve "status": "falha" (ignore quando o status for "sucesso").
Retorne (ou imprima) uma lista apenas com os IPs suspeitos de ataque de 
Força Bruta (Brute Force) — ou seja, qualquer IP que tenha tido 3 ou 
mais falhas.

(No exemplo acima, o IP "192.168.1.10" teve 3 falhas e 1 sucesso, então 
 ele deve ser detectado como atacante).

Regras do Jogo:
Nada de pedir para IA gerar.
Não use bibliotecas externas (como pandas ou Counter). Use apenas Python 
puro (for, if, dicionário {} ou lista []).
Se travar na sintaxe, me pergunte a dúvida pontual, mas quem escreve o 
código é você.

Valendo! Como você escreve essa função detectar_forca_bruta(logs)? 
Pode mandar o código aqui quando terminar.
'''



logs_acesso = [
    {"ip": "192.168.1.10", "usuario": "admin", "status": "falha"},
    {"ip": "10.0.0.5", "usuario": "maria", "status": "sucesso"},
    {"ip": "192.168.1.10", "usuario": "admin", "status": "falha"},
    {"ip": "192.168.1.10", "usuario": "root", "status": "falha"},
    {"ip": "172.16.0.2", "usuario": "joao", "status": "falha"},
    {"ip": "172.16.0.2", "usuario": "joao", "status": "falha"},
    {"ip": "172.16.0.2", "usuario": "joao", "status": "falha"},
    {"ip": "172.16.0.2", "usuario": "joao", "status": "falha"},
    {"ip": "172.16.0.2", "usuario": "joao", "status": "falha"},
    {"ip": "172.16.0.2", "usuario": "joao", "status": "falha"},
    {"ip": "10.0.0.8", "usuario": "admin", "status": "falha"},
    {"ip": "192.168.1.10", "usuario": "admin", "status": "sucesso"},
]

def detectar_forca_bruta(logs):

    ips = []
    for i in logs:
        if i['status'] == 'falha':
            ips.append(i['ip'])
    suspeitos = {}
    for ip in ips:
        if ips.count(ip) >= 3:
            if ip not in suspeitos:
                suspeitos[ip] = ips.count(ip)
    print(f'IPs Suspeito: ', suspeitos)

detectar_forca_bruta(logs_acesso)