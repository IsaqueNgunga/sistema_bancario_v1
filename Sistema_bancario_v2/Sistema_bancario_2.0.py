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
   
   print("--------------------------------------------------")

   if valor > 0:
      saldo += valor
      extrato += f"\n Deposito: R$ {valor: .2f}\n"
      print("\n Depositgo relaizado! \n\n Você será redirecionado ao menu principal.\n")
      
   else:
        print("\n Opção indisponível. \n\n Favor digitar um valor positivo. \n\n Você será redirecionado ao menu principal. \n")

   print("--------------------------------------------------")

   return saldo, extrato

def withdraw(*,saldo, valor, extrato, SAQUES_DIARIOS, LIMIT_SAQUE, numero_saques):
   saque_indisponivel = numero_saques >= SAQUES_DIARIOS
   limit_exedido = valor > LIMIT_SAQUE

   print("--------------------------------------------------")
   
   if limit_exedido:
            print("\n Limite exedido! \n\n Saque R$500,00 ou menos. \n\n Você será redirecionado ao menu principal.")

   elif valor < 0:
            print("\n Operação inválida! \n\n Digite um valor positivo. \n\n Você será redirecionado ao menu principal.")

   elif saque_indisponivel:
            print("\n Saques diários esgotados! \n\n Aguarde 24h para realizar uma nova transação. \n\n Você será redirecionado ao menu principal.")

   elif valor <= saldo:
            saldo -= valor
            extrato += f"\nSaque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\n Transação realizada. \n\n Valor: R$ {valor:.2f} \n\n Retire seu dinheiro na boca do caixa. \n\n Você será redirecionado ao menu principal.\n")
            

   elif valor > saldo:
            print("\n Saldo insuficiente. \n\n Você será redirecionado ao menu principal.")

   print("--------------------------------------------------")
    
   return saldo, extrato, numero_saques

def register(usuario):
     
     cpf = str(input("\n Informe seu cpf:"))
     
     verify = search_cpf(cpf, usuario)

     if verify:
          print("\n\n O CPF informado pertence a um usuário. Digite um CPF válido. \n\n Você será redirecionado ao menu principal \n ")
          print("--------------------------------------------------")
          return

     nome = input("\n\n Informe seu nome completo:")
     
     d_nacimento = input("\n\n Informe sua data de nacimento:")
     
     endereco = (input("\n\n Logradouro:"), input("\n\n Numero:"), input("\n\n Bairro:"), input("\n\n Cidade/Estado:"))

     usuario.append({"Nome": nome, "Data de Nacimento": d_nacimento, "CPF": cpf, "Endereço": endereco})

     print("\n--------------------------------------------------")
     
     print(f"\n Seja bem vindo a DS Banck {nome}!\n\n Abaixo dados cadastrais\n\n {usuario} \n\n Você será redirecionado ao menu principal \n")
     
     print("--------------------------------------------------")

     return nome, d_nacimento, cpf, endereco

def search_cpf(cpf, usuario):
     verification = [verify for verify in usuario if verify["CPF"] == cpf]
     return verification[0] if verification else None

def account(usuario, AGENCIA, n_account):
     
     cpf = input("Informe o CPF do usuário: ")
     verify = search_cpf(cpf, usuario)

     if verify:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": AGENCIA, "numero_conta": n_account, "usuario": usuario}

     print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
          


def main():
 SAQUES_DIARIOS = 3
 LIMIT_SAQUE = 500
 AGENCIA = "0001"

 saldo = 0
 extrato = ""
 numero_saques = 0
 usuario = []
 contas = []
 n_account = 0
 
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
     register(usuario)

  elif opcao == "5":
            n_account = len(contas) + 1
            conta = account(usuario, AGENCIA, n_account)

            if conta:
                contas.append(conta)

  elif opcao == "0":
     break
main()