def menu():
    menu = """
 ================= MENU =================

               [1] Extrato
               [2] Depositar
               [3] Sacar
               [4] Cadastro
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
    
   return saldo, extrato, numero_saques

def cadastro():
     usuario = []
     nome = input("\n Informe seu nome completo:")
     d_nacimento = input("\n Informe sua data de nacimento:")
     cpf = input("\n Informe seu cpf:")
     endereco = input("\n Informe seu endereço:")
     
     add_nome = usuario.append(nome)
     add_nacimento = usuario.append(d_nacimento)
     add_cpf = usuario.append(cpf)
     add_endereco = usuario.append(endereco)

     print(f"\n Seja bem vindo a DS Banck {nome}!\n\n Abaixo dados cadastrais\n\n {usuario}")

     return nome, d_nacimento, cpf, endereco


def main():
 SAQUES_DIARIOS = 3
 LIMIT_SAQUE = 500

 saldo = 0
 extrato = ""
 numero_saques = 0
 usuarios = {}
 
 while True:
  opcao = menu()

  if opcao == "1":
    extract(saldo, extrato=extrato)

  elif opcao == "2":
      valor = float(input("Informe o valor do deposito:"))
      saldo, extrato = deposit(saldo, valor, extrato)
  
  elif opcao == "3":
      valor = float(input("Informe o valor do saque: "))
      
      saldo, extrato, numero_saques = withdraw(
           saldo=saldo,
           valor=valor,
           extrato=extrato,
           SAQUES_DIARIOS=SAQUES_DIARIOS,
           LIMIT_SAQUE=LIMIT_SAQUE,
           numero_saques=numero_saques,
           )
  
  elif opcao == "4":
      usuarios = cadastro()


  elif opcao == "0":
     break
main()