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

saldo = 0
limite = 500
numero_saques = 0
extrato = ""
def xextrato(saldo, /, *, extrato):
    print("\n================= EXTRATO =================")
    print("Não foram realizadas movimentaçoes." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")

def main():
 
 while True:
  opcao = menu()

  if opcao == "1":
    xextrato(saldo, extrato=extrato)

  elif opcao == "0":
     break
main()