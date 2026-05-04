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

def processar_compra(escolha, s, saldo):
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
                    return s, saldo
                else:
                    print("não tem em estoque",x["estoque"])
            else:
                s = input("Deseja continuar (s/n):")
                return s, saldo
        
def mostrarRelatorio(saldo):
    print("Produtos comprados",carrinho)
    print("Valor a pagar",saldo)
    for x in armas:
        print("Nome:",x["nome"],"Estoque",x["estoque"])
        
def caixa_eletronico():
    saldo = 0
    continuar = 's'
    while continuar == 's':
        print("|| Lista de armas||")
        for arma in armas:
            print("Nome:",arma["nome"],"Tipo:",arma["tipo"],"Valor(R$):",arma["preco"])            
        try:
            escolha = input(("Escolha sua arma:"))
            nomes = [a["nome"]for a in armas]
            if escolha not in nomes:
                print("Não temos essa arma")
            else:
                continuar, saldo = processar_compra(escolha, continuar, saldo)
        except ValueError:
            print("Escolha dentre essas opções")    
    mostrarRelatorio(saldo)
caixa_eletronico()
     