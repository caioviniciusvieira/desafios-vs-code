print("1 - adicionar item\n2 - remover um item\n3 - ver lista\n4 - sair")
produtos = []

def main():

    while True:   
        opcao = int(input("Escolha uma opção:"))

        if opcao == 1:
            adicionar()
        elif opcao == 2:
            remover()
        elif opcao == 3:
            ver_lista()
        elif opcao == 4:
            escolha = input("Deseja sair y/n:")
            if escolha == "y" or escolha == "yes":
                exit()
        else:
            print("opção não existe tentar novamente")

def adicionar ():
    produto = input("Nome do produto que deseja adiconar: ")
    produtos.append(produto)

def remover():
    pedido = input("Nome do produto que deseja remover: ")
    produto = None
    for x in produtos:
        if pedido == x:
            produto = x
    if produto == pedido:
        produtos.remove(produto)        
    else:
        print("Produto não encontrado")

def ver_lista():
    if not produtos:
        print("Não adicionou nenhum produto")
    else:
        print(produtos)

main()