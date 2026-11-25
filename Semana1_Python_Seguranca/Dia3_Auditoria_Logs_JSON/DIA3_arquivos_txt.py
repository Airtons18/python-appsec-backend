

def auditar_arquivo_log(logs):
    with open(logs, 'r', encoding='utf-8') as arquivo:
        relatorio_ataques = []
        for linha in arquivo:
            linha = linha.strip()
            partes = linha.split(' | ')
            if (len(partes) == 4):
                
                if ('403' in partes[3] or '404' in partes[3]):
                    relatorio_ataques.append(partes)

    with open('relatorio_ataques.txt', 'w', encoding='utf-8') as relatorio:
        for linha in relatorio_ataques:
            relatorio.write(f'IP: {linha[1]} | Alvo: {linha[2]} | Status: {linha[3]}\n')
                        


auditar_arquivo_log('acessos_servidor.log')
