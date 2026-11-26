
def verificar_prompt_injection(text):
    black_words = ['ignore as instruções', 'delete from', 'mostre a senha']
    cmd = text.lower()
    encontrou = False
    for palavras in black_words:
        if palavras in cmd:
            encontrou = True
    if encontrou == True:
        return True
    else:
        return False
    

def ocultar_dados_sensiveis(dic_log):
    dic_sanitizado = []
        
    if 'cpf' and 'api_key' in dic_log:
        dic_log['cpf'] = '***OCULTO***'
        dic_log['api_key'] = '***OCULTO***'
        dic_sanitizado.append(dic_log)
    return dic_sanitizado

