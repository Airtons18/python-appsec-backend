import json

class ContaUsuario:

    # 1. Construtor roda quando cria o objeto e quarda os dados iniciais em self.
    def __init__(self, usuario, senha_correta):
        self.usuario = usuario
        self.senha_correta = senha_correta
        self.token_recuperacao = 'TOKEN-999'
        self.historico_logs = []
        self.tentativas_falhas = 0
        self.bloqueado = False

    # 2. Funções dentro da classe.
    def tentar_login(self, senha_digitada):
        if self.bloqueado == True:

            self.historico_logs.append('Tentativa em conta bloqueada')

            print(f'ACESSO NEGADO! Conta bloqueada!')

            return False
        
        elif senha_digitada == self.senha_correta:

            self.tentativas_falhas = 0
            self.historico_logs.append('Login Aprovado')

            print('LOGIN APROVADO!')

            return True
        else:
            self.tentativas_falhas += 1
            self.historico_logs.append('Falha de Senha')
            
            if self.tentativas_falhas >= 3:
                self.bloqueado = True
                self.historico_logs.append('Conta Bloqueada!')

            print(f'SENHA INCORRETA! Tentativas: {self.tentativas_falhas}')
            return False

    # 3. Desbloquear a conta.
    def desbloquear_conta(self, token_informado, nova_senha):

        if token_informado == self.token_recuperacao:
            if nova_senha != self.senha_correta and len(nova_senha) >= 8:
                self.senha_correta = nova_senha
                self.bloqueado = False
                self.tentativas_falhas = 0
                self.historico_logs.append("Conta Desbloqueada e senha alterada")
                print('CONTA DESBLOQUEADA COM SUCESSSO!')
                return True
            else:
                print('NOVA SENHA FRACA OU IGUAL À ANTERIOR!')
                return False
        else:
            print('TOKEN INVÁLIDO!')
            return False

    def exportar_auditoria_json(self):
        relatorio = {
            "usuario": self.usuario,
            "bloqueado": self.bloqueado,
            "tentativa_falhas": self.tentativas_falhas,
            "historico_logs": self.historico_logs
        }

        nome_arquivo = f'audotira_{self.usuario}.json'

        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(relatorio, arquivo, indent=4, ensure_ascii=False)
            arquivo.close()

        print(f'Relatório exportado: {nome_arquivo}')



class ContaAdmin(ContaUsuario):
    def __init__(self, usuario, senha_correta, nivel_acesso):
        super().__init__(usuario, senha_correta)
        self.nivel_acesso = nivel_acesso
        self.status_risco = ""
        self.total_logs = 0
        
    def executar_comando_critico(self, comando):
        if self.bloqueado == True:
            self.historico_logs.append("Tentativa com conta Bloqueada!")
            return False
        elif self.nivel_acesso < 5:
            self.historico_logs.append("Alerta: Tentativa de Escalada de Privilégio")
            print(f"ALERTA DE SEGURANCA (Privilege Escalation): Nivel Insuficiente para executar {comando}")
            return False
        else:
            print(f'Comando executado: {comando}')
            self.historico_logs.append(f'COMANDO CRÍTICO EXECUTADO: {comando}')
            return True

    def auditar_seguranca_admin(self):

        if "Alerta: Tentativa de Escalada de Privilégio" in self.historico_logs or self.bloqueado == True:
            self.status_risco = "ALTO"

        else:
            self.status_risco = "BAIXO"

        self.total_logs = len(self.historico_logs)
        print(f'STATUS RISCO: {self.status_risco} Usuario: {self.usuario}, Total logs: {self.total_logs}')            
        resposta = {
            "STATUS": self.status_risco, 
            "TOTAL": self.total_logs
            }
        return resposta


conta_admin = ContaUsuario("admin_airton", "Segredo@2026")

conta_admin.tentar_login("123456")       # Erro 1

conta_admin.tentar_login("admin123")      # Erro 2
conta_admin.tentar_login("senha_errada")  # Erro 3 -> Aqui tem que bloquear a conta!
conta_admin.tentar_login("Segredo@2026")  # Tentativa 4 (COM A SENHA CERTA!) -> Tem que dar CONTA BLOQUEADA!
# Tentando desbloquear com token errado:
conta_admin.desbloquear_conta("TOKEN-ERRADO", "NovaSenha@2027")

# Tentando desbloquear com senha curta demais (menos de 8 letras):
conta_admin.desbloquear_conta("TOKEN-999", "123")

# Desbloqueando do jeito certo:
conta_admin.desbloquear_conta("TOKEN-999", "NovaSenha@2027")

# Testando login com a senha nova:
conta_admin.tentar_login("NovaSenha@2027")

# Imprimindo toda a trilha de auditoria da conta:
print("Histórico de Auditoria:", conta_admin.historico_logs)

print("-" * 50)
# Criando um Admin Júnior (Nível 2) e um Super Admin (Nível 5):
admin_jr = ContaAdmin("airton_jr", "SenhaForte@1", 2)
super_admin = ContaAdmin("airton_root", "Root@2026!", 5)

# Admin Jr tentando apagar o banco (Tem que dar ALERTA de Privilege Escalation!):
admin_jr.executar_comando_critico("DROP DATABASE clientes")

# Super Admin executando comando legítimo (Tem que funcionar!):
super_admin.executar_comando_critico("REINICIAR_FIREWALL")

print("Logs Admin Jr:", admin_jr.historico_logs)
print("Logs Super Admin:", super_admin.historico_logs)
conta_admin.exportar_auditoria_json()
admin_jr.exportar_auditoria_json()
super_admin.exportar_auditoria_json()
admin_jr.auditar_seguranca_admin()
super_admin.auditar_seguranca_admin()