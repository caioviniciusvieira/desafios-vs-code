def lista(numbers):
    maior = 0
    for x in numbers:
        if x > maior:
            maior = x
    return maior        

print(lista([2,6,7]))