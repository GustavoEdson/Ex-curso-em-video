#034
salario = int(input('Qual é o seu salario? '))
base = 1250
soma_a = salario + (salario *10 / 100)
soma_d = salario + (salario *15 / 100)

if salario > base:
    print('Seu slario ganhou um aumento de 10%, salario atual: {:.2f}'.format(soma_a))

if salario <= base:
    print('Você vai ganhar um aumento de 15%, Salario atual: {:.2f}'.format(soma_d))