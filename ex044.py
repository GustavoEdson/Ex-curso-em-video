#044
print('{:=^40}'.format(' Lojas Gugu! '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTOS
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão 
[ 3 ] 2x no cartão 
[ 4 ] 3x no cartão''')  
opcao = int(input('Qual é a opção?: '))
if opcao == 1:
    total = preço - (preço * 10 / 100)
elif opcao == 2:
    total = preço - (preço * 10 / 100)
elif opcao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parceladas em tantas {}x de {:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = 0
    print('OPÇÃO INVALIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar de R${:.2f} no final.'.format(preço, total))