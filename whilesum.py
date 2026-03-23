def sum_numbers():
    resultado = 0
    while True:
        try:
            num = float(input("Digite umm número(-1 para sair):"))

            if num == -1:
                break

            resultado += num

        except ValueError:
            print("Digite apenas números inteiros:")


    return resultado

total = sum_numbers()
print("Total da soma é:",total)
