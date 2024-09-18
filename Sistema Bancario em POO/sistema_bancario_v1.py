from abc import ABC, abstractmethod

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

# class Conta_corrente(Conta):