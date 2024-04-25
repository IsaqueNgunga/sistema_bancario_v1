def menu():
    menu = """
 ================= MENU =================

               [1] Extrato
               [2] Depositar
               [3] Sacar
               [4] Cadastro
               [5] Conta
               [6] Listar contatos
               [0] Sair

 ========================================
 => """
    return input(f"\n Seja bem vindo a DS Bank! \n\n Como posso lhe ajudar? \n {menu}")

def extract(saldo, /, *, extrato):
    print("\n================= EXTRATO =================\n")
    print("\n Não foram realizadas movimentaçoes." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f} \n\n Você será redirecionado ao menu principal.")
    print("\n===========================================\n")

def deposit(saldo,valor,extrato,/):
   
   if valor > 0:
      saldo += valor
      extrato += f"\n Deposito: R$ {valor: .2f}\n"
      print("\n Depositgo relaizado! \n\n Você será redirecionado ao menu principal.\n")
      
   else:
        print("\n Opção indisponível. \n\n Favor digitar um valor númerico positivo. \n\n Você será redirecionado ao menu principal. \n")

   return saldo, extrato

def withdraw(*,saldo, valor, extrato, SAQUES_DIARIOS, LIMIT_SAQUE, numero_saques):
   saque_indisponivel = numero_saques >= SAQUES_DIARIOS
   limit_exedido = valor > LIMIT_SAQUE
   
   if limit_exedido:
            print("\n Limite exedido! \n\n Saque R$500,00 ou menos. \n\n Você será redirecionado ao menu principal.")

   elif valor < 0:
            print("\n Operação inválida! \n\n igite um valor positivo. \n\n Você será redirecionado ao menu principal.")

   elif saque_indisponivel:
            print("\n Saques diários esgotados! \n\n Aguarde 24h para realizar uma nova transação. \n\n Você será redirecionado ao menu principal.")

   elif valor <= saldo:
            saldo -= valor
            extrato += f"\nSaque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\n Transação realizada. \n\n Valor: R$ {valor:.2f} \n\n Retire seu dinheiro na boca do caixa. \n\n Você será redirecionado ao menu principal.\n")
            

   elif valor > saldo:
            print("\n Saldo insuficiente. \n\n Você será redirecionado ao menu principal.")
    
   return saldo, extrato, numero_saques

def cadastro(usuarios):
     usuario = []
     nome = input("\n Informe seu nome completo:")
     d_nacimento = input("\n\n Informe sua data de nacimento:")
     cpf = input("\n\n Informe seu cpf:")
     endereco = input("\n\n Informe seu endereço:")
     
     add_nome = usuario.append({"Nome": nome})
     add_nacimento = usuario.append({"Data de Nacimento": d_nacimento})
     add_cpf = usuario.append({"CPF": cpf})
     add_endereco = usuario.append({"Endereço": endereco})

     print(f"\n Seja bem vindo a DS Banck {nome}!\n\n Abaixo dados cadastrais\n\n {usuario}")

     return nome, d_nacimento, cpf, endereco

def main():
 SAQUES_DIARIOS = 3
 LIMIT_SAQUE = 500
 AGENCIA = "0001"

 saldo = 0
 extrato = ""
 numero_saques = 0
 usuarios = {}
 contas = []
 
 while True:
  opcao = menu()

  if opcao == "1":
    extract(saldo, extrato=extrato)

  elif opcao == "2":
      valor = float(input(" Informe o valor do deposito:"))
      saldo,extrato = deposit(saldo, valor, extrato)
  
  elif opcao == "3":
      valor = float(input(" Informe o valor do saque: "))
      
      saldo, extrato, numero_saques = withdraw(
           saldo=saldo,
           valor=valor,
           extrato=extrato,
           SAQUES_DIARIOS=SAQUES_DIARIOS,
           LIMIT_SAQUE=LIMIT_SAQUE,
           numero_saques=numero_saques,
           )
  
  elif opcao == "4":
      usuarios = cadastro(usuarios)

  elif opcao == "0":
     break
main()