
def mensagem():
    banco = "DS BANK"
    mensagem = f"\n Seja bem vindo a {banco}! \n"
    return mensagem

def menu():
    menu = """
 ================= MENU =================

               [1] Extrato
               [2] Depositar
               [3] Sacar
               [0] Sair

 ========================================
 => """
    return input(f"\n Como posso lhe ajudar? \n {menu}")

def extract(saldo, /, *, extrato):
    print("\n================= EXTRATO =================\n")
    print("Não foram realizadas movimentaçoes." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")

def deposit(saldo,valor,extrato,/):
   
   if valor > 0:
      saldo += valor
      extrato += f"\nDeposito: R$ {valor: .2f}\n"
      return saldo, extrato

def withdraw(*,saldo, valor, extrato, SAQUES_DIARIOS, LIMIT_SAQUE, numero_saques):
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
            extrato += f"\nSaque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\nTransação realizada. Valor: R$ {valor:.2f} Retire seu dinheiro na boca do caixa.\n")
            

   elif valor > saldo:
            print("Saldo insuficiente.")
    
   return saldo, extrato


def main():
 saldo = 0
 extrato = ""
 SAQUES_DIARIOS = 3
 LIMIT_SAQUE = 500
 numero_saques = 0
 
 while True:
  opcao = menu()

  if opcao == "1":
    extract(saldo, extrato=extrato)

  elif opcao == "2":
      valor = float(input("Informe o valor do deposito:"))
      saldo, extrato = deposit(saldo, valor, extrato)
  
  elif opcao == "3":
      valor = float(input("Informe o valor do saque: "))
      
      saldo, extrato = withdraw(
           saldo=saldo,
           valor=valor,
           extrato=extrato,
           SAQUES_DIARIOS=SAQUES_DIARIOS,
           LIMIT_SAQUE=LIMIT_SAQUE,
           numero_saques=numero_saques,
           )


  elif opcao == "0":
     break
main()