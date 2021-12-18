print('-'*20)
print('LOJA DO GUGU')
print('-'*20)
soma = 0
mais_caro = 0
while True:
    produto = str(input('Nome do protudo: '))
    preco = int(input('Preço: '))
    soma += preco
    pergunta = str(input('Quer continuar? [S/N]')).strip().upper()
    if preco >= 1000:
        mais_caro += 1
    if pergunta == 'N':
        print(f'O total da compra foi {soma}')
        print(f'Temos {mais_caro} podutos custando mais de 1000 reais.')
        break
