# Exercício Python #055, Maior e menor da sequência
for p in range(1, 6):
    peso = input('Qual é o peso da {} pessoa: '.format(p))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso lido foi {}Kg'.format(maior))
print('o menor peso lido foi {}Kg'.format(menor))