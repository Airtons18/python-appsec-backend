import json



def auditar_arquivo_log(logs):

    with open(logs, 'r', encoding='utf-8') as arquivo:
        relatorio_ataques = []
        resumo_por_ip = {}
        for linha in arquivo:
            linha = linha.strip()
            partes = linha.split(' | ')
            if (len(partes) == 4):
                if ('403' in partes[3] or '404' in partes[3]):
                    evento = {
                        "data": partes[0],
                        "ip": partes[1],
                        "alvo": partes[2],
                        "status": int(partes[3])  # Converte o status '403' para número inteiro 403!
                    }
                    relatorio_ataques.append(evento)
                    end_ip = partes[1]
                    if end_ip not in resumo_por_ip:
                        resumo_por_ip[end_ip] = 1
                    else:
                        resumo_por_ip[end_ip] += 1
                    dados_finais = {
                        "total_ataques": len(relatorio_ataques),
                        "contagem_por_ip": resumo_por_ip,
                        "eventos": relatorio_ataques
                    }
    with open("alertas_seguranca.json", 'w', encoding='utf-8') as arquivo:
        json.dump(dados_finais, arquivo, indent=4, ensure_ascii=False)
        arquivo.close()

auditar_arquivo_log('acessos_servidor.log')
