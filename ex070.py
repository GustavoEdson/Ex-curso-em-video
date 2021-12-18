print('-'*20)
print('LOJA DO GUGU')
print('-'*20)
soma = mais_caro = mais_barato = cont = 0
barato = ''
while True:
    produto = str(input('Nome do protudo: '))
    preco = int(input('Preço: R$'))
    cont += 1
    soma += preco
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if preco >= 1000:
        mais_caro += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
           menor = preco
           barato = produto
    if resposta == 'N':
        print(f'O total da compra foi {soma}')
        print(f'Temos {mais_caro} podutos custando mais de 1000 reias.')
        print(f'o produto mais barato foi {barato} e custa {menor:.2f} ')
        break