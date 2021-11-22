#038
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
primeiro = n1
segundo = n2

if n1 > n2:
    print('O PRIMEIRO numero é maior que {}'.format(n2))
elif n1 < n2:
    print('O SEGUNDO numero é maior que {}'.format(n1))
else:
    print('dois numeros são iguais')