def depositar(x):
    while True:
        try:     
            deposito = float(input("Digite a quantidade a depositar:"))
            x += deposito
            return x
        except:
            print("Digite apenas números")
def sacar(x):
    while True:
        try:
            while True:
                saque = float(input("Digite a quantidade a sacar:"))
                if x < saque:
                    print("Saldo insuficiente")
                else:
                    x -= saque
                    return x    
        except:
            print("Digite apenas números")

def caixa_eletronico():
    while True:
        try:
            saldo = float(input("Digite seu saldo:"))
            break
        except ValueError:
            print("digite apenas números")

    while True:
            print("(1)Depositar (2)Sacar (3)Sair")
            try:
                escolha = int(input(("Escolha:")))
                if escolha == 1:
                    saldo = depositar(saldo)
                elif escolha == 2:
                    saldo = sacar(saldo)
                elif escolha == 3:
                    print("Seu saldo",saldo)
                    break
                else:
                    print("Não existe opção")
            except ValueError:
                print("Escolha dentre essas opções")

caixa_eletronico()     