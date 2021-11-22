#036
casa = float(input('Qual é o valor da casa: R$'))
salario = float(input('Qual é o seu salário: R$'))
anos = float(input('Em quantos voce vai pagar: R$'))
#formulas
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print('para pagar a casa uma casa de R${:.2f} em {} anos'.format(casa, anos),end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('emprestimo concedido!')
else:
    print('emprestimo negado!')