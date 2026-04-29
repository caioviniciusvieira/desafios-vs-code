armas = [
    {
        "nome": "1911",
        "tipo": "pistola",
        "preco": 500.00,
        "estoque": 5
    },
    {
        "nome": "mp5",
        "tipo": "submetralhadora",
        "preco": 450.00,
        "estoque": 10
    },
    {
        "nome": "ak47",
        "tipo": "rifle de assalto",
        "preco": 800.00,
        "estoque": 20
    }
]
carrinho = []

def mostrarRelatorio():
    for x in armas:
        print("Nome:",x["nome"],"Estoque",x["estoque"])
        

def caixa_eletronico():
    saldo = 0
    s = 's'
    while s == 's':
            print("|| Lista de armas||")
            for arma in armas:
                print("Nome:",arma["nome"],"Tipo:",arma["tipo"],"Valor(R$):",arma["preco"])
            try:
                escolha = input(("Escolha sua arma:"))
                for x in armas:
                    if x["nome"] == escolha:
                        arma = escolha
                        respota = input("deseja comprar essa arma s/n:")
                        if respota == 's':
                            if x["estoque"] > 0:
                                x["estoque"] -=1
                                saldo += x["preco"]
                                carrinho.append(arma)
                                s = input("Deseja continuar (s/n):")
                            else:
                                print("não tem em estoque",x["estoque"])
                if arma != escolha:
                    print("Não temos essa arma")
            except ValueError:
                print("Escolha dentre essas opções")
    print("Produtos comprados",carrinho)
    print("Valor a pagar",saldo)
    
mostrarRelatorio()
caixa_eletronico()
     