import random
vida = 20
armadura = 15
bonus = 5

def calcular_acerto(resultado):
    ataque = resultado + bonus
    if ataque > armadura:
        print("Você acertou!")
    else:
        print("Você errou")

def rodar_dado(valor,dado):
    valor = random.randint(1,dado)
    return valor

def escolher_dado():
    print("(1)1d20, (2)1d6, (3)1d8")
    escolha = int(input(":"))
    dado = 0
    resultado=0
    if escolha == 1:
        dado = 20
        resultado = rodar_dado(resultado,dado)
        print("Tirou:",resultado)
        calcular_acerto(resultado)
    elif escolha == 2:
        dado = 6
        resultado = rodar_dado(resultado,dado)
        print("Tirou:",resultado)
        calcular_acerto(resultado)
    else:
        dado = 8
        resultado = rodar_dado(resultado,dado)
        print("Tirou:",resultado)
        calcular_acerto(resultado)

escolher_dado()