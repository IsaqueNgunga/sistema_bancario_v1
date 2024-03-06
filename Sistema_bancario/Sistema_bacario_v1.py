menu = """
================= MENU =================

               [1] Extrato
               [2] Depositar
               [3] Sacar
               [0] Sair

========================================
=> """

saldo = 0
extrato = ""
SAQUES_DIARIOS = 3
LIMIT_SAQUE = 500
numero_saques = 0
banco = "DS BANK"

mensagem = f"Bem vindo a {banco}!"
print(mensagem)


while True:
    opcao = input(menu)

    if opcao == "1":
        print("\n================= EXTRATO =================")
        print("Não foram realizadas movimentaçoes." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        
        print("=============================================")

    elif opcao == "2":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("Operação inválida, digite um valor positivo.")

    elif opcao == "3":
        valor = float(input("Informe o valor do saque: "))
       
        saque_indisponivel = numero_saques >= SAQUES_DIARIOS
        limit_exedido = valor > LIMIT_SAQUE

        if limit_exedido:
            print("Limite exedido! Saque R$500,00 ou menos.")

        elif valor < 0:
            print("Operação inválida, digite um valor positivo")

        elif saque_indisponivel:
            print("Saques diários esgotados! Aguarde 24h para realizar uma nova trasação.")

        elif valor <= saldo:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Transação realizada. Valor: R$ {valor:.2f} Retire seu dinheiro na boca do caixa.")
            

        elif valor > saldo:
            print("Saldo insuficiente.")

        

    elif opcao == "0":
        break