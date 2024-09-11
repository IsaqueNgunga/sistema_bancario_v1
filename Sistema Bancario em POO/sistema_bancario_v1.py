from abc import ABC, abstractmethod

class Cliente:
    def __init__(self,endereco, contas):
        
        contas = []
        self._endereco = endereco
        self._contas = contas

    def realizar_trasacao(self, conta, transacao):
        transacao.registrar(conta)

        def adicionar_conta(self, conta):
            self._contas.append(conta)

class Pessoa_Fisica(Cliente):
    def __init__(self, cpf, nome, data_nacimento):
        
        self._cpf = cpf
        self._nome = nome
        self._data_nacimento = data_nacimento
        super()._endereco
        
    @property
    def Idade(self):
        _ano_atual = 2024
        return _ano_atual -self._data_nacimento
    
class Conta:
    def __init__(self,saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico