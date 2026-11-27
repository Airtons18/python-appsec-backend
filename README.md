# 🛡️ Python AppSec & Back-end Lab

Laboratório prático de **Engenharia de Software Back-end e Segurança de Aplicações (AppSec)** desenvolvido 100% em **Python puro** (sem dependências externas prontas de análise e sem código gerado por IA), com foco no domínio sólido de algoritmos, estruturas de dados, Programação Orientada a Objetos (POO), Bancos de Dados SQL e prevenção de vulnerabilidades.

---

## 🎯 Objetivo do Repositório

Construir, módulo a módulo, ferramentas reais de **Monitoramento de Segurança (SIEM), Web Application Firewall (WAF), Controle de Acesso (IAM/RBAC), Sanitização de Dados e Persistência Segura em Banco de Dados**, aplicando na prática os princípios do **OWASP Top 10**.

---

## 📂 Estrutura do Projeto

```text
python-appsec-backend/
├── README.md
└── Semana1_Python_Seguranca/
    ├── Dia1_Forca_Bruta/
    │   └── DIA1.py
    ├── Dia2_Firewall_e_Lentidao/
    │   ├── DIA2_port_scan.py
    │   └── DIA2_lentidao_logs_sujos.py
    ├── Dia3_Auditoria_Logs_JSON/
    │   ├── acessos_servidor.log
    │   ├── DIA3_arquivos_txt.py
    │   ├── DIA3_exportar_json.py
    │   ├── relatorio_ataques.txt
    │   └── alertas_seguranca.json
    ├── Dia4_Modulos_Prompt_Injection/
    │   ├── validador_seguranca.py
    │   └── DIA4_principal.py
    └── Dia5_Bloqueio_Conta/
        ├── Dia5_poo.py
        ├── audotira_admin_airton.json
        ├── audotira_airton_jr.json
        └── audotira_airton_root.json
```

---

## 📋 Catálogo de Módulos e Contexto de Engenharia

### 🔹 Semana 1 — Fundamentos de Python, Manipulação de Logs & POO Aplicada à Segurança

#### 1. Detecção de Ataque de Força Bruta (`Dia1_Forca_Bruta`)
* **Contexto (OWASP A07 - Identification and Authentication Failures):** Correlação de eventos de falha de login para identificar tentativas automatizadas de adivinhação de credenciais (*Brute Force*).
* **Implementação (`DIA1.py`):** Filtra eventos com `"status": "falha"` e agrega a contagem de falhas por endereço IP em dicionário, isolando atacantes com 3 ou mais tentativas sem duplicidade de alertas.

#### 2. Scanner de Portas de Firewall & Tolerância a Logs Corrompidos (`Dia2_Firewall_e_Lentidao`)
* **Contexto (Reconhecimento & DoS):** Detecção de *Port Scanning* (`21`, `22`, `3306`, `8080`) em logs brutos de firewall e identificação de rotas com lentidão crítica (`>= 2000 ms`) em arquivos com falhas de rede/linhas truncadas.
* **Implementação (`DIA2_port_scan.py` & `DIA2_lentidao_logs_sujos.py`):** Parsing de strings com `.split(':')`, acumuladores nativos em dicionário e programação defensiva (`len()`, `.isdigit()`, `try/except`) para processar logs sujos sem interromper a execução.

#### 3. Auditoria de Servidor Web e Exportação para SIEM (`Dia3_Auditoria_Logs_JSON`)
* **Contexto (Fuzzing & Integração SIEM):** Monitoramento de requisições HTTP `403` e `404` geradas por varreduras em busca de arquivos sensíveis (`/.env`, `/wp-admin.php`, `/backup.sql`, `/config.php`).
* **Implementação (`DIA3_arquivos_txt.py` & `DIA3_exportar_json.py`):** Leitura de `acessos_servidor.log` em loop único, geração de relatório legível (`relatorio_ataques.txt`) e serialização estruturada em `alertas_seguranca.json` contendo métricas globais, contagem por IP e lista de eventos.

#### 4. Arquitetura Modular, Prevenção de *Prompt Injection* e LGPD (`Dia4_Modulos_Prompt_Injection`)
* **Contexto (OWASP LLM01 & LLM06):** Proteção de sistemas integrados a IA contra instruções maliciosas (*"ignore as instruções"*, *"delete from"*, *"mostre a senha"*) e sanitização de credenciais/dados pessoais antes da gravação de logs.
* **Implementação (`validador_seguranca.py` & `DIA4_principal.py`):** Separação de responsabilidades em módulo importado, normalização de texto (`.lower()`), varredura de *blacklist* e mascaramento automático de `cpf` e `api_key` (`***OCULTO***`).

#### 5. POO: Cofre de Autenticação, MFA, RBAC e *Privilege Escalation* (`Dia5_Bloqueio_Conta`)
* **Contexto (OWASP A01 & A07 / IAM):** Gestão de estado de contas de usuário e administradores com bloqueio automático após 3 falhas (*Account Lockout*), recuperação via Token MFA e prevenção de Escalada de Privilégio.
* **Implementação (`Dia5_poo.py`):** Superclasse `ContaUsuario` e subclasse `ContaAdmin(ContaUsuario)` com herança via `super().__init__()`, trilha de auditoria interna (`self.historico_logs`), validação de política de senha forte (`len >= 8` e inédita), restrição de comandos críticos a administradores `nivel_acesso >= 5`, classificação dinâmica de risco e exportação individual em JSON.



---

**Autor:** Airton Aparecido dos Santos Neto  
[GitHub](https://github.com/Airtons18)
[LinkedIn](https://www.linkedin.com/in/airton-santos-5815261b8/)
