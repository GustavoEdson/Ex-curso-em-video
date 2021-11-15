#012
preço = float(input('Digite seu preço R$'))
novo = preço - (preço * 5 / 100)
parcelado = preço + (preço *5 / 100)


print('O produto que custava {:.2f}R$ na promoção com desconto de 5%, vai custar: {:.2f} a vista'.format(preço, novo))
print('se voce pagar parcelado vai sair com uma taxa de 5% a mais que no total da {}'.format(parcelado))