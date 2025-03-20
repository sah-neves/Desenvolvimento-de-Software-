from datetime import date

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)
    
    def mostrar_transacoes(self):
        for t in self.transacoes:
            print(t)

class Transacao:
    def registrar_transacao(self, conta):
        raise NotImplementedError("Subclasse deve implementar este método")

class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar_transacao(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(f"Depósito de R${self.valor:.2f}")
    
class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor
    
    def registrar_transacao(self, conta):
        if conta.saldo >= self.valor:
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(f"Saque de R${self.valor:.2f}")
            return True
        else:
            return False

class Conta:
    def __init__(self, saldo: float, numero: int, agencia: str, cliente):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def get_saldo(self):
        return self.saldo

    def nova_conta(self, cliente, numero):
        return Conta(self.saldo, cliente, numero)

    def sacar(self, valor: float):
        saque = Saque(valor)
        if saque.registrar_transacao(self):
            return f"Saque de R${valor:.2f} realizado com sucesso!"
        else:
            return "Saldo insuficiente!"

    def depositar(self, valor: float):
        if valor > 0:
            deposito = Deposito(valor)
            deposito.registrar_transacao(self)
            return f"Depósito de R${valor:.2f} realizado com sucesso!"
        else:
            return "Valor de depósito inválido!"

class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        return transacao.registrar_transacao(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, limite: float, limite_saque: int):
        super().__init__(saldo, numero, agencia, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

# Testando o código
cliente1 = PessoaFisica(cpf="123.456.789-00", nome="João Silva", data_nascimento=date(1990, 1, 1), endereco="Rua A, 123")
conta_corrente = ContaCorrente(saldo=1000.0, numero=12345, agencia="001", cliente=cliente1, limite=500.0, limite_saque=3)
cliente1.adicionar_conta(conta_corrente)

# Realizando transações
resultado_deposito = conta_corrente.depositar(200.0)
print(resultado_deposito)

resultado_saque = conta_corrente.sacar(150.0)
print(resultado_saque)

saldo_atual = conta_corrente.get_saldo()
print(f"Saldo atual: R${saldo_atual:.2f}")

resultado_saque_insuficiente = conta_corrente.sacar(1200.0)
print(resultado_saque_insuficiente)

# Exibindo o histórico de transações
print("\nHistórico de Transações:")
conta_corrente.historico.mostrar_transacoes()
