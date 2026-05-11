carrinho = [80,100,90,120,130]
saldo = 0

def descont(item, preco_final):
    desconto = item+(item*0.15)
    preco_final+= desconto
    return desconto, preco_final

for i in range(len(carrinho)):
    if carrinho[i] > 100:
        carrinho[i], saldo = descont(carrinho[i], saldo)
    else:
        saldo+=carrinho[i]
        

print(saldo, carrinho)
        