def smallest_number(numbers):
    menor = numbers[0]
    for x in numbers:
        if x < menor:
            menor = x

    return menor

print(smallest_number([2,1,3]))
