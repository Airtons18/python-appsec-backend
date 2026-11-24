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
    └── Dia2_Firewall_e_Lentidao/
        ├── DIA2_port_scan.py
        └── DIA2_lentidao_logs_sujos.py
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



---

**Autor:** Airton Aparecido dos Santos Neto  
[GitHub](https://github.com/Airtons18)
[LinkedIn](https://www.linkedin.com/in/airton-santos-5815261b8/)
