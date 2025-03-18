from datetime import date

class Conta:
    def __init__(self,saldo:float,numero:int,agencia:str,cliente,historico):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia 
        self.cliente = cliente 
        self.historico = historico

    def get_saldo(self):
        return self.saldo
    
    def nova_conta(self,cliente,numero):
        pass

    def sacar(self,valor:float):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.registrar_transacao(f"Saque de R${valor}")
            return f"Saque de R${valor} realizado com sucesso!"
        else:
            return "Saldo insuficiente!"

    def depositar(self, valor:float):
        if valor > 0:
            self.saldo += valor
            self.historico.registrar_transacao(f"Depósito de R${valor}")
            return f"Depósito de R${valor} realizado com sucesso!"
        else:
            return "Valor de depósito inválido!"

class Cliente:
    def __init__(self, endereco:str, contas):
        self.endereco = endereco 
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        pass

    def adicionar_conta(self, conta):
        return self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf:str, nome:str, data_nascimento: date):
        self.cpf = cpf
        self.nome = nome 
        self.data_nascimento = data_nascimento

class Historico:
    def __init__(self):
        self.transacoes = []
                 
class Transacao:
    def __init__(self):
        pass

    def registrar_transacao(self, conta):
        pass
        
class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite:float,limite_saque:int):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self.limite = limite 
        self.limite_saque = limite_saque 
