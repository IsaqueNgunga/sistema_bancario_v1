from abc import ABC, abstractmethod, abstractpropety
from datetime import datetime

class Cliente:
    def __init__(self,endereco, contas):
        
        contas = []
        self.endereco = endereco
        self.contas = contas

    def realizar_trasacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
            self.contas.append(conta)

class Pessoa_Fisica(Cliente):
    def __init__(self, cpf, nome, data_nacimento,endereco):
        
        self.cpf = cpf
        self.nome = nome
        self.data_nacimento = data_nacimento
        super().__init__(endereco)
        
        
    @property
    def Idade(self):
        _ano_atual = 2024
        return _ano_atual - self.data_nacimento
    
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()


    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def hitorico(self):
        self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Limite excedido")

        elif saldo >= valor:
            self._saldo -= valor
            print("Saque realizado")
            return True

        else:
            print("Operação inválida")
            return False
        
    def depositar(self, valor):
        negativo = valor <= 0
        
        if negativo:
            print("Digite um valor positivo")
            return False
        
        elif valor >= 0:
            print("Depósito realizado")
            return True
        
        else:
            print("Operação invalida")

class Conta_corrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        self.limite = limite
        self.limite_saques = limite_saques  

    def sacar(self, valor):
        
        numero_saques = len(
            [transacao for transacao in self._historico.transacao["tipo"] = saque.__name__]
            )
        
        excede_limete = valor >= self.limite
        excede_limete_saque = valor >= self.limite_saques

        if excede_limete:
            print("Limite insuficiente, retire R$500 ou menos")

        elif excede_limete_saque:
            print("Saques diários encerrados.")

        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agencia:\t{self.agencia}
            c\c:\t\t{self.numero}
            Titular:\t{self.cliente}
        """
    
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self.transacoes
    
    def adicionar_transacoes(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class Transacao(ABC):

    @property
    @abstractpropety
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = 

        @property
        def valor(self):
            return self._valor
        
        def registrar(self, conta):
            sucesso_transacao = conta.sacar(self.valor)

            if sucesso_transacao:
             conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)