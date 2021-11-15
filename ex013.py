#013
salário = float(input('Qual é o salário do Funcionario? R$'))

novo = salário + (salário * 15 / 100)

print('Um funcionario que ganhava {:.2f}R$ com 15% de desconto, passa a receber {:.2f}R$'.format(salário, novo))