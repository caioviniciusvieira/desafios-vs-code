import random
number = random.randint(1,20)

tentativas = 0
pontos = 9
while True:
    try:
        guess = int(input("Advinhe o número de  (1 a 20):"))
        tentativas+=1
        pontos -= 2
        if guess == number:
            print(f"Você acertou em {tentativas} tentativas")
            print("Pontos:",pontos)
            break
        elif guess < number:
            print("Muito baixo")
        else:
            print("Muito alto")

    except ValueError:
        print("Digite apenas números inteiros")
       
